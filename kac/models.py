from django.db import models
from django.contrib.auth.models import AbstractUser


class UpdatedUser(AbstractUser):
    my_key = models.CharField(max_length=100, default='abcd')
