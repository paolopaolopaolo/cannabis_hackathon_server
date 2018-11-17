
from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import HighProfile


class SignUpRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')


class UpdateProfile(serializers.ModelSerializer):

    class Meta:
        model = HighProfile
        fields = ()
