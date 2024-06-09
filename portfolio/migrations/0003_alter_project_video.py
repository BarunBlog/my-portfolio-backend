# Generated by Django 5.0.6 on 2024-06-03 08:55

import portfolio.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='my-portfolio/projects/videos/', validators=[portfolio.validators.validate_video_file_extension]),
        ),
    ]
