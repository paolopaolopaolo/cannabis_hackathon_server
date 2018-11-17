from django.contrib.auth.models import User
from django.db import models


class HighProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    recommendation = models.TextField()

    @property
    def is_owner(self):
        return hasattr(self, 'vendor')


class Vendor(models.Model):
    owner = models.OneToOneField(HighProfile, related_name='vendor', on_delete=models.CASCADE)
