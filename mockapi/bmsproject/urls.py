# urls.py

from django.urls import path
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('api/projects/', ProjectListView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]
