from django.db import models

# Create your models here.

class Goals(models.Model):
    goal = models.CharField(max_length=50)
    status = models.CharField(default = True)


def __str__(self):
    return self.goal



