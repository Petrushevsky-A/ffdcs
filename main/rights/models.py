from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class AccessType(models.Model):
    title = models.CharField(max_length=50, unique=True)

class AccessService(models.Model):
    title = models.CharField(max_length=50, unique=True)

class AccessLevel(models.Model):
    title = models.CharField(max_length=50, unique=True)
    priority = models.SmallIntegerField(validators=[MinValueValidator(0),MinValueValidator(10)])

class Access(models.Model):
    access_type = models.ForeignKey(
        AccessType,
        null=True,
        on_delete=models.SET_NULL,
    )
    access_service = models.ForeignKey(
        AccessService,
        null=True,
        on_delete=models.SET_NULL,
    )
    access_level = models.ForeignKey(
        AccessLevel,
        null=True,
        on_delete=models.SET_NULL,
    )
    id_how_to = models.IntegerField()
