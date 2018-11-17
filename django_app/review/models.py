from django.db import models
from user.caliva import *

# Create your models here.
from user.models import HighProfile


class Review(models.Model):
    user = models.ForeignKey(HighProfile, related_name='reviews', on_delete=models.CASCADE)
    product_id = models.IntegerField()
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    rating = models.PositiveSmallIntegerField()

    @property
    def get_product(self):
        search_for_products(self.product_id)
        ## TODO: Emmanual to insert all this

        pass


class Tag(models.Model):
    review = models.ForeignKey(Review, related_name='tags', on_delete=models.CASCADE)
    content = models.CharField(max_length=20, default='')

