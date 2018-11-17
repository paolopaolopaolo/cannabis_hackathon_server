from django.contrib.auth.models import User
from django.db import models


class HighProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)

    @property
    def is_vendor_owner(self):
        return hasattr(self, 'vendor')

    @property
    def is_distributor_owner(self):
        return hasattr(self, 'distributor')

    @property
    def is_owner(self):
        return self.is_distributor_owner or self.is_vendor_owner


class Vendor(models.Model):
    owner = models.OneToOneField(HighProfile, related_name='vendor', on_delete=models.CASCADE)


class Distributor(models.Model):
    owner = models.OneToOneField(HighProfile, related_name='distributor', on_delete=models.CASCADE)
