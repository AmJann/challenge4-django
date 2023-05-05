from django.db import models
from user.models import *

# Create your models here.
class List(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    list_name = models.CharField(max_length=50, null=True)


class ListItems (models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    resturant_id = models.CharField(max_length=30)
    resturant_categories = models.CharField(max_length=500)
    resturant_distance = models.DecimalField(max_digits=17, decimal_places=13)
    resturant_url = models.CharField(max_length=500, null=True)
    resturant_rating = models.DecimalField(max_digits=9, decimal_places=6)
    user_rating = models.DecimalField(max_digits=9, decimal_places=6)