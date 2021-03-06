
from django.contrib.auth.models import User
from rest_framework import serializers


class SignUpRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

