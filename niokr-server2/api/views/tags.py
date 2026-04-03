from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Tag
from ..serializers import TagSerializer


class TagPagination(PageNumberPagination):
    page_size = 5


class TagsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tags = Tag.objects.all()
        paginator = TagPagination()
        if 'page' not in request.query_params:
            serializer = TagSerializer(tags, many=True)
            return Response({'count': tags.count(), 'results': serializer.data})

        page = paginator.paginate_queryset(tags, request)
        serializer = TagSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, _, pk):
        try:
            tag = Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            return Response({'detail': 'Тег не найден.'}, status=status.HTTP_404_NOT_FOUND)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
