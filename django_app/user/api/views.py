from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from user.api.serializers import SignUpRequestSerializer
from user.models import HighProfile


class UserViewSet(ViewSet):

    @swagger_auto_schema(methods=['post'], request_body=SignUpRequestSerializer)
    @action(methods=['POST'], detail=False)
    def signup(self, request):
        serializer = SignUpRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = {
            **serializer.data,
            'username': serializer.data.get('email')
        }
        password = serializer.data.pop('password')
        user = User.objects.create(**data)
        user.set_password(password)
        user.save()
        HighProfile.objects.create(user=user)
        return Response(data={'result': user.pk}, status=201)

