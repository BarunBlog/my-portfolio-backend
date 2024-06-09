from rest_framework import generics
from .models import Experience
from .serializers import ExperienceSerializer


class ExperienceList(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
