from django.contrib import admin

# Register your models here.
from review.models import Tag, Review

admin.site.register(Tag)
admin.site.register(Review)
