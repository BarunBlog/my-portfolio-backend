from django.urls import path
from .views import ExperienceList

urlpatterns = [
    path('get-experiences/', ExperienceList.as_view(), name="get_experiences"),
]
