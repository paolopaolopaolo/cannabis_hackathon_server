from django.contrib.auth.models import User
from django.test import TestCase
from user.models import HighProfile, Vendor


class UserTestCase(TestCase):

    def test_user_vendor_relationship(self):
        me = User.objects.create(username='dean@me.io', email='dean@me.io')
        me_profile = HighProfile.objects.create(user=me)
        Vendor.objects.create(owner=me_profile)
        self.assertTrue(me_profile.is_owner)

        me2 = User.objects.create(username='dean+12@me.io', email='dean+12@me.io')
        me_profile2 = HighProfile.objects.create(user=me2)
        self.assertFalse(me_profile2.is_owner)
