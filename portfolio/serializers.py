from rest_framework import serializers
from .models import Project


class ProjectListSerializer(serializers.ModelSerializer):

    project_image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['uuid', 'name', 'small_description', 'project_type', 'project_image']

    def get_project_image(self, obj):
        request = self.context.get('request')
        first_image = obj.images.first()
        if first_image:
            image_url = first_image.image.url  # This returns relative url
            return request.build_absolute_uri(image_url)  # This returns absolute url with the domain
        return None


class ProjectDetailSerializer(serializers.ModelSerializer):
    project_images = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['uuid', 'name', 'small_description', 'description', 'technologies_used', 'project_type', 'url',
                  'repository_url', 'video', 'start_date', 'end_date', 'project_images', 'conclusion']

    def get_project_images(self, obj):
        request = self.context.get('request')
        image_urls = [request.build_absolute_uri(image.image.url) for image in obj.images.all()]
        return image_urls
