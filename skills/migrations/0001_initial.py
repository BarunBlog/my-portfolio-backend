# Generated by Django 5.0.6 on 2024-05-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skill_level', models.CharField(choices=[('Beg', 'Beginner'), ('Int', 'Intermediate'), ('Expd', 'Experienced'), ('Adv', 'Advanced'), ('Exp', 'Expert')], max_length=20)),
                ('skill_type', models.CharField(choices=[('programming_language', 'Programming Language'), ('backend', 'Backend Technologies'), ('frontend', 'Frontend Technologies'), ('devops_and_deployment', 'DevOps and Deployment'), ('messaging_and_task_queues', 'Messaging and Task Queues'), ('testing', 'Testing'), ('version_control', 'Version Control'), ('operating_systems', 'Operating Systems')], max_length=50)),
            ],
        ),
    ]
