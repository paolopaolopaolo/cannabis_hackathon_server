from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from review.models import Review
from user.caliva import Caliva


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


@method_decorator(swagger_auto_schema(operation_description='POST /api/v1/review'), name='create')
class ReviewViewSet(ModelViewSet):
    queryset = Review
    serializer_class = ReviewSerializer

class ProductViewSet(ViewSet):

    @action(methods=['GET'], detail=False)
    def products(self, request):
        caliva_api = Caliva()
        # TODO: Return all products from Caliva
        products = caliva_api.search_for_products()
        print(products)
        return Response(data={'result': products}, status=200)

