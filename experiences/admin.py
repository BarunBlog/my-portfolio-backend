from django.contrib import admin
from .models import Experience, Responsibility


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'employer_name', 'post_name', 'start_date', 'end_date']


class ResponsibilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'experience', 'responsibility']


admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Responsibility, ResponsibilityAdmin)