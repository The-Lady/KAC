from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email_id = models.CharField(max_length=200, null=True, blank=False)
    username = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200, null=True, blank=False)