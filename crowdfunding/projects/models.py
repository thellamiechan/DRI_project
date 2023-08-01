from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.CharField(max_length=200)

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
         'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.CharField(max_length=200) 

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
