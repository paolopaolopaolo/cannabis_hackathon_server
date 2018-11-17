from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product_id = models.IntegerField()
    body = models.TextField()
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    rating = models.PositiveSmallIntegerField()


class Tag(models.Model):
    review = models.ForeignKey(Review, related_name='tags', on_delete=models.CASCADE)

