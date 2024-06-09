from django.urls import path
from .views import SkillList

urlpatterns = [
    path('get-skills/', SkillList.as_view(), name="get_skills"),
]
