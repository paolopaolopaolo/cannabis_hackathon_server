from django.contrib.auth.models import User
from django.test import TestCase
from user.models import HighProfile, Vendor


class UserTestCase(TestCase):

    def test_user_vendor_relationship(self):
        me = User.objects.create(email='dean@me.io')
        me_profile = HighProfile.objects.create(user=me)
        Vendor.objects.create(owner=me_profile)
        self.assertTrue(me_profile.is_owner)
