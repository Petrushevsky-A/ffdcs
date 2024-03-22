from django.db import models

class InterfaceType(models.Model):
    title = models.CharField(max_length=50, unique=True)


class InterfaceService(models.Model):
    title = models.CharField(max_length=50, unique=True)
    interface_type = models.ForeignKey(
        InterfaceType,
        null=True,
        on_delete=models.SET_NULL,
    )

class InterfaceLevel(models.Model):
    title = models.CharField(max_length=50, unique=True)


class Interface:
    service = models.ForeignKey(
        InterfaceService,
        null=True,
        on_delete=models.SET_NULL,
    )
    id_how_to = models.IntegerField()

 
