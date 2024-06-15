# Generated by Django 5.0.6 on 2024-06-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0004_alter_skill_skill_level_alter_skill_skill_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_type',
            field=models.CharField(choices=[('Programming Language', 'Programming Language'), ('Backend', 'Backend Technologies'), ('Frontend', 'Frontend Technologies'), ('Database', 'Database'), ('DevOps & Deployment', 'DevOps and Deployment'), ('Messaging & Task Queues', 'Messaging and Task Queues'), ('Testing', 'Testing'), ('Version Control', 'Version Control'), ('Operating Systems', 'Operating Systems')], max_length=50),
        ),
    ]
