import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
# from .validators import validate_video_file_extension
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from tinymce.models import HTMLField

PROJECT_TYPE_CHOICES = (
    ('frontend', 'frontend'),
    ('backend', 'backend'),
    ('full-stack', 'full-stack'),
)


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    small_description = models.CharField(max_length=50)
    description = HTMLField()
    technologies_used = ArrayField(models.CharField(max_length=100), blank=True)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES)
    url = models.URLField(max_length=200, null=True, blank=True)
    repository_url = models.URLField(max_length=200, null=True, blank=True)
    video = models.FileField(upload_to='my-portfolio/projects/videos/',
                             null=True, blank=True, storage=VideoMediaCloudinaryStorage())
    conclusion = HTMLField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='my-portfolio/projects/images/')
    # no need to set storage, field will use the default one from settings

    def __str__(self):
        return f"Image for {self.project.name}"

    def image_url(self):
        return self.image.url
