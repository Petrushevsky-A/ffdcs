from django.db import models

class ServiceType(models.Model):
    title = models.CharField(max_length=50, unique=True)

class Service(models.Model):

    title = models.CharField(max_length=50, unique=True)
    path = models.CharField(max_length=50, unique=True)
    type =  models.ForeignKey(
        ServiceType,
        null=True,
        on_delete=models.SET_NULL,
    )
