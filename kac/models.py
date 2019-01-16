from django.db import models
from django.contrib.auth.models import AbstractUser


class UpdatedUser(AbstractUser):
    my_key = models.CharField(max_length=100, default='abcd')


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()