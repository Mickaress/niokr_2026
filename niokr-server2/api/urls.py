from django.urls import path

from .views import (
    ProjectsView,
    ProjectView,
    FilesView,
    ProjectApplicationView,
    ProjectApplicantsView,
    MeView,
    TagsView,
    TagView,
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('me', MeView.as_view(), name='me'),
    path('projects', ProjectsView.as_view(), name='projects-list'),
    path('project/<int:pk>', ProjectView.as_view(), name='project-detail'),
    path('project/<int:pk>/apply', ProjectApplicationView.as_view(), name='project-apply'),
    path('project/<int:pk>/applicants', ProjectApplicantsView.as_view(), name='project-applicants'),
    path('project/<int:pk>/files', FilesView.as_view(), name='project-files'),
    path('project/<int:pk>/files/<int:file_pk>', FilesView.as_view(), name='project-file-detail'),
    path('tags', TagsView.as_view(), name='tags-list'),
    path('tag/<int:pk>', TagView.as_view(), name='tag-detail'),
]