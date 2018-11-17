
from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import HighProfile


class SignUpRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')


class UpdateProfile(serializers.ModelSerializer):

    profile_type = serializers.CharField(max_length=3)

    class Meta:
        model = HighProfile
        fields = ('profile_type, ')
