from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.postgres.fields import JSONField

class Role(MPTTModel):
    title = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    info = JSONField()

class TypeStructure(models.Model):
    title = models.CharField(max_length=30, blank=True)

class Organization(MPTTModel):
    title = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    type = models.ForeignKey(
        TypeStructure,
        on_delete=models.SET_NULL,
    )
    info = JSONField()

class TypeUser(models.Model):
    title = models.CharField(max_length=30, blank=True)

class User(AbstractUser):
    # ИДЕЯ При удалении дочерней роли переключает в родительскую с понижением прав.
    role = models.ForeignKey(
        Role,
        null=True,
        on_delete=models.SET_NULL,
    )
    # ИДЕЯ При удалении дочерней структуры переключает в родительскую c понижением прав.
    organization = models.ForeignKey(
        Role,
        null=True,
        on_delete=models.SET_NULL,
    )
    type = models.ForeignKey(
        TypeUser,
        null=True,
        on_delete=models.SET_NULL,
    )
