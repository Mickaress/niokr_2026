import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import F, Q, Count
from ..models import Project, File, Tag, ProjectApplication, UserProfile, EmployeeProfile
from ..serializers import (
    ProjectSerializer,
    ProjectListSerializer,
    FileSerializer,
    ProjectApplicantSerializer,
)

class ProjectPagination(PageNumberPagination):
    page_size = 3


class ProjectsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        role = request.user.profile.role
        if role == 'customer':
            projects = Project.objects.filter(company__customer=request.user.profile)
        elif role == 'employee':
            employee = request.user.profile.employee
            projects = Project.objects.filter(
                Q(status=Project.Status.ACTIVE) | Q(employee=employee)
            ).distinct()
        elif role == 'admin':
            projects = Project.objects.all()
        else:
            return Response({'detail': 'Недостаточно прав.'}, status=status.HTTP_403_FORBIDDEN)

        if name_filter := request.query_params.get('name'):
            projects = projects.filter(name__icontains=name_filter)
        tag_ids = []
        for key in ('tags', 'tags[]'):
            for raw in request.query_params.getlist(key):
                if not raw:
                    continue
                for part in raw.split(','):
                    part = part.strip()
                    if part.isdigit():
                        tag_ids.append(int(part))
        tag_ids = list(dict.fromkeys(tag_ids))
        if tag_ids:
            projects = projects.filter(tags__id__in=tag_ids).distinct()
        if status_filter := request.query_params.get('status'):
            if status_filter in {s.value for s in Project.Status}:
                projects = projects.filter(status=status_filter)
        if role == 'employee' and request.query_params.get('is_applied') == 'true':
            projects = projects.filter(applications__employee=employee).distinct()

        projects = projects.annotate(applications_count=Count('applications__id', distinct=True))

        paginator = ProjectPagination()
        page = paginator.paginate_queryset(projects, request)

        serializer = ProjectListSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if request.user.profile.role != 'customer':
            return Response({'detail': 'Недостаточно прав.'}, status=status.HTTP_403_FORBIDDEN)

        customer_profile = request.user.profile
        try:
            company = customer_profile.company
        except Exception:
            return Response({'detail': 'У заказчика нет компании.'}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data

        raw_tag_ids = data.get('tagIds', [])
        # tagIds может приходить либо строкой JSON, либо списком (например, [] или [1,2]).
        if isinstance(raw_tag_ids, str):
            try:
                tag_ids = json.loads(raw_tag_ids)
            except (json.JSONDecodeError, TypeError):
                return Response({'detail': 'Некорректный формат tagIds.'}, status=status.HTTP_400_BAD_REQUEST)
        elif isinstance(raw_tag_ids, list):
            tag_ids = raw_tag_ids
        else:
            return Response({'detail': 'Некорректный формат tagIds.'}, status=status.HTTP_400_BAD_REQUEST)

        # нормализуем: только int/числа
        try:
            tag_ids = [int(t) for t in tag_ids]
        except (TypeError, ValueError):
            return Response({'detail': 'Некорректный формат tagIds.'}, status=status.HTTP_400_BAD_REQUEST)

        project = Project.objects.create(
            name=data.get('name'),
            description=data.get('description', ''),
            date_start=data.get('dateStart') or None,
            date_end=data.get('dateEnd') or None,
            company=company,
        )

        if tag_ids:
            project.tags.set(Tag.objects.filter(id__in=tag_ids))

        files = request.FILES.getlist('files')
        for f in files:
            File.objects.create(project=project, file=f, original_filename=f.name)

        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if request.user.profile.role == UserProfile.Role.EMPLOYEE:
            Project.objects.filter(pk=pk, status=Project.Status.ACTIVE).update(views=F('views') + 1)
        project = Project.objects.annotate(applications_count=Count('applications__id', distinct=True)).get(pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'detail': 'Проект не найден.'}, status=status.HTTP_404_NOT_FOUND)

        user_profile = request.user.profile
        is_admin = user_profile.role == UserProfile.Role.ADMIN
        is_project_customer = (
            user_profile.role == UserProfile.Role.CUSTOMER and project.company.customer_id == user_profile.id
        )

        if not (is_admin or is_project_customer):
            return Response({'detail': 'Недостаточно прав.'}, status=status.HTTP_403_FORBIDDEN)

        if project.status == Project.Status.ARCHIVED:
            return Response(
                {'detail': 'Нельзя изменять архивный проект.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = request.data.copy()
        employee_id = data.pop('employee_id', None)
        if isinstance(employee_id, list):
            employee_id = employee_id[0] if employee_id else None
        if employee_id is not None:
            if not is_admin:
                return Response({'detail': 'Назначать исполнителя может только администратор.'}, status=status.HTTP_403_FORBIDDEN)
            if employee_id in ('', 'null', None):
                project.employee = None
                project.save(update_fields=['employee'])
            else:
                try:
                    employee = EmployeeProfile.objects.get(pk=int(employee_id))
                except (ValueError, TypeError, EmployeeProfile.DoesNotExist):
                    return Response({'detail': 'Исполнитель не найден.'}, status=status.HTTP_400_BAD_REQUEST)
                project.employee = employee
                project.save(update_fields=['employee'])

        serializer = ProjectSerializer(project, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, _, pk):
        files = File.objects.filter(project_id=pk)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        project = Project.objects.get(pk=pk)
        uploaded_files = request.FILES.getlist('files')
        if not uploaded_files:
            return Response({'detail': 'Файлы не переданы.'}, status=status.HTTP_400_BAD_REQUEST)
        created = []
        for f in uploaded_files:
            file_obj = File.objects.create(
                project=project,
                file=f,
                original_filename=f.name,
            )
            created.append(file_obj)
        serializer = FileSerializer(created, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, _, pk, file_pk):
        file_obj = File.objects.get(pk=file_pk, project_id=pk)
        file_obj.file.delete(save=False)
        file_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectApplicationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        if request.user.profile.role != UserProfile.Role.EMPLOYEE:
            return Response({'detail': 'Недостаточно прав.'}, status=status.HTTP_403_FORBIDDEN)

        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'detail': 'Проект не найден.'}, status=status.HTTP_404_NOT_FOUND)

        employee = request.user.profile.employee
        _, created = ProjectApplication.objects.get_or_create(project=project, employee=employee)
        if created:
            return Response({'detail': 'Отклик отправлен.'}, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Вы уже откликнулись на этот проект.'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if request.user.profile.role != UserProfile.Role.EMPLOYEE:
            return Response({'detail': 'Недостаточно прав.'}, status=status.HTTP_403_FORBIDDEN)

        try:
            employee = request.user.profile.employee
            application = ProjectApplication.objects.get(project_id=pk, employee=employee)
        except ProjectApplication.DoesNotExist:
            return Response({'detail': 'Отклик не найден.'}, status=status.HTTP_404_NOT_FOUND)

        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectApplicantsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(_, request, pk):
        try:
            project = Project.objects.select_related('company__customer').get(pk=pk)
        except Project.DoesNotExist:
            return Response({'detail': 'Проект не найден.'}, status=status.HTTP_404_NOT_FOUND)

        user_profile = request.user.profile
        is_admin = user_profile.role == UserProfile.Role.ADMIN

        if not is_admin:
            return Response({'detail': 'Недостаточно прав.'}, status=status.HTTP_403_FORBIDDEN)

        applications = (
            ProjectApplication.objects
            .filter(project_id=pk)
            .select_related('employee__profile__user')
            .prefetch_related('employee__tags')
            .order_by('-id')
        )
        serializer = ProjectApplicantSerializer(applications, many=True)
        return Response(serializer.data)
