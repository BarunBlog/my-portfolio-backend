from django.contrib import admin
from .models import Project, ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid', 'technologies_used', 'start_date', 'end_date']


class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'image']


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
