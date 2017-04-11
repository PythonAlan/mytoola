from django.db import models

# Create your models here.
class WorkPlace(models.Model):
    project_name = models.CharField(max_length=80)
    project_link = models.URLField(null=False)

    def __str__(self):
        return self.project_name