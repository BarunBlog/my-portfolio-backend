from django.db import models

SKILL_LEVEL_CHOICES = (
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Experienced", "Experienced"),
    ("Advanced", "Advanced"),
    ("Expert", "Expert"),
)

SKILL_TYPE_CHOICES = (
    ("Programming Language", "Programming Language"),
    ("Backend", "Backend Technologies"),
    ("Frontend", "Frontend Technologies"),
    ("Database", "Database"),
    ("DevOps & Deployment", "DevOps and Deployment"),
    ("Messaging & Task Queues", "Messaging and Task Queues"),
    ("Testing", "Testing"),
    ("Version Control", "Version Control"),
    ("Operating Systems", "Operating Systems"),
)


class Skill(models.Model):
    name = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)
    skill_type = models.CharField(max_length=50, choices=SKILL_TYPE_CHOICES)

    class Meta:
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name
