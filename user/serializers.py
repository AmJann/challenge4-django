from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    username1 = serializers.ReadOnlyField(source = "user1.username")
    username2 = serializers.ReadOnlyField(source = "user2.username")
    username3 = serializers.ReadOnlyField(source = "user3.username")
    username4 = serializers.ReadOnlyField(source = "user4.username")

    class Meta:
        model = Groups
        fields = ['pk','group_name','user1','user2','user3','user4','username1','username2','username3','username4']

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields ='__all__'




