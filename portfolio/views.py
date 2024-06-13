from rest_framework import generics
from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-start_date')
    serializer_class = ProjectListSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'uuid'

    def get_serializer_context(self):
        return {'request': self.request}
