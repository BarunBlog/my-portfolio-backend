from rest_framework import generics
from .models import Skill
from .serializers import SkillSerializer


class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
