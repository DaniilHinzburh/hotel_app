from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    password = models.CharField(max_length=255)
    passport = models.IntegerField()
    address = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255, null=True)
    is_admin = models.BooleanField(default=False)
