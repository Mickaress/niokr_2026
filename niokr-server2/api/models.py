from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .utils import project_file_upload_path, MAX_LENGTH_FIELD, MAX_LENGTH_TEXT


class UserManager(BaseUserManager):
    def create_user(self, external_id, **extra_fields):
        user = self.model(external_id=external_id, **extra_fields)
        user.set_unusable_password()
        user.save()
        return user


class User(AbstractBaseUser):
    external_id = models.CharField(max_length=MAX_LENGTH_FIELD, unique=True)
    full_name = models.CharField(max_length=MAX_LENGTH_FIELD, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=MAX_LENGTH_FIELD, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'external_id'

    objects = UserManager()


class UserProfile(models.Model):
    class Role(models.TextChoices):
        CUSTOMER = 'customer'
        EMPLOYEE = 'employee'
        ADMIN = 'admin'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=Role.choices)


class Company(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_FIELD)
    address = models.CharField(max_length=MAX_LENGTH_FIELD, blank=True)
    description = models.TextField(max_length=MAX_LENGTH_TEXT, blank=True)
    customer = models.OneToOneField(UserProfile, on_delete=models.PROTECT, related_name='company')


class Tag(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_FIELD)


class EmployeeProfile(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='employee')
    competencies = models.TextField(max_length=MAX_LENGTH_TEXT, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='employees')


class Project(models.Model):
    class Status(models.TextChoices):
        REVIEW = 'review'
        ACTIVE = 'active'
        ARCHIVED = 'archived'

    name = models.CharField(max_length=MAX_LENGTH_FIELD)
    description = models.TextField(max_length=MAX_LENGTH_TEXT, blank=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='projects')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.REVIEW)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='projects')
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class ProjectApplication(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications')
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, related_name='applications')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project', 'employee'], name='unique_project_employee')
        ]


class File(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to=project_file_upload_path)
    original_filename = models.CharField(max_length=MAX_LENGTH_FIELD)
    uploaded_at = models.DateTimeField(auto_now_add=True)

