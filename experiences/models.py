from django.db import models


class Experience(models.Model):
    employer_name = models.CharField(max_length=200)
    post_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.employer_name


class Responsibility(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='responsibilities')
    responsibility = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = 'Responsibilities'

    def __str__(self):
        return str(self.pk)

