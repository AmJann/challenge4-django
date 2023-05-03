from rest_framework import serializers
from .models import *


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'

class ListItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItems
        fields = '__all__'

