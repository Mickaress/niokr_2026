from rest_framework import serializers
from .models import Project, File, User, EmployeeProfile, Company, Tag, ProjectApplication


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'address', 'description']


class CompanyProjectSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = [
            'name',
            'address',
            'description',
            'customer',
        ]

    def get_customer(self, obj):
        user = obj.customer.user
        return {
            'full_name': user.full_name,
            'email': user.email,
            'phone': user.phone,
        }


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='profile.role')
    company = CompanySerializer(source='profile.company')
    tags = serializers.SerializerMethodField()
    competencies = serializers.CharField(source='profile.employee.competencies')

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone', 'role', 'company', 'tags', 'competencies']

    def get_tags(self, instance):
        if instance.profile.role == 'employee':
            return list(instance.profile.employee.tags.values_list('id', flat=True))
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.profile.role != 'customer':
            data.pop('company', None)
        if instance.profile.role != 'employee':
            data.pop('tags', None)
            data.pop('competencies', None)
        return data


class UserUpdateSerializer(serializers.Serializer):
    full_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)

    # customer
    company_name = serializers.CharField(required=False)
    company_address = serializers.CharField(required=False)
    company_description = serializers.CharField(required=False)

    # employee
    competencies = serializers.CharField(required=False)
    tags = serializers.ListField(child=serializers.IntegerField(), required=False)

    def update(self, instance, validated_data):
        for field in ('full_name', 'email', 'phone'):
            if field in validated_data:
                setattr(instance, field, validated_data[field])
        instance.save()

        role = instance.profile.role

        if role == 'customer':
            company = instance.profile.company
            for field in ('company_name', 'company_address', 'company_description'):
                if field in validated_data:
                    setattr(company, field.removeprefix('company_'), validated_data[field])
            company.save()

        elif role == 'employee':
            employee = instance.profile.employee
            if 'competencies' in validated_data:
                employee.competencies = validated_data['competencies']
                employee.save()
            if 'tags' in validated_data:
                employee.tags.set(Tag.objects.filter(id__in=validated_data['tags']))

        return instance


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'original_filename', 'uploaded_at']
        read_only_fields = ['original_filename', 'uploaded_at']

    def create(self, validated_data):
        uploaded_file = validated_data['file']
        validated_data['original_filename'] = uploaded_file.name
        return super().create(validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    company = CompanyProjectSerializer()
    files = FileSerializer(many=True, read_only=True)
    period = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    applications_count = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'period', 'tags', 'status', 'company', 'created_at', 'files', 'views', 'applications_count']

    def get_period(self, obj):
        parts = [str(obj.date_start) if obj.date_start else None,
                 str(obj.date_end) if obj.date_end else None]
        parts = [p for p in parts if p]
        return ' - '.join(parts) if parts else None
    
    def get_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y')

    def get_applications_count(self, obj):
        if hasattr(obj, 'applications_count'):
            return obj.applications_count
        return obj.applications.count()


class ProjectListSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    period = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    is_applied = serializers.SerializerMethodField()
    applications_count = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'period', 'tags', 'status', 'company', 'created_at', 'is_applied', 'applications_count']

    def get_company(self, obj):
        return {'name': obj.company.name}

    def get_period(self, obj):
        parts = [str(obj.date_start) if obj.date_start else None,
                 str(obj.date_end) if obj.date_end else None]
        parts = [p for p in parts if p]
        return ' - '.join(parts) if parts else None

    def get_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y')

    def get_is_applied(self, obj):
        request = self.context.get('request')
        if not request or request.user.profile.role != 'employee':
            return None
        try:
            employee = request.user.profile.employee
        except EmployeeProfile.DoesNotExist:
            return False
        return ProjectApplication.objects.filter(project=obj, employee=employee).exists()

    def get_applications_count(self, obj):
        if hasattr(obj, 'applications_count'):
            return obj.applications_count
        return obj.applications.count()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data.get('is_applied') is None:
            data.pop('is_applied')
        return data


class ProjectApplicantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='employee.id')
    full_name = serializers.CharField(source='employee.profile.user.full_name')

    class Meta:
        model = ProjectApplication
        fields = ['id', 'full_name']

    def get_tags(self, obj):
        return list(obj.employee.tags.values_list('id', flat=True))