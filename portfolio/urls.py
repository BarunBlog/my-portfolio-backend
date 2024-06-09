from django.urls import path
from .views import ProjectList, ProjectDetail

urlpatterns = [
    path('projects/get-projects/', ProjectList.as_view(), name="get_projects"),
    path('projects/<uuid:uuid>/', ProjectDetail.as_view(), name='project_detail'),
]
