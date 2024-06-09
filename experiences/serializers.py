from rest_framework import serializers
from .models import Experience, Responsibility


class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility
        fields = ['responsibility']


class ExperienceSerializer(serializers.ModelSerializer):
    responsibilities = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = ['employer_name', 'post_name', 'start_date', 'end_date', 'responsibilities']

    def get_responsibilities(self, obj):
        return [responsibility.responsibility for responsibility in obj.responsibilities.all()]