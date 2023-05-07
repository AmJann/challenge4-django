from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

user_status = (
    ('GC', 'Group Creator'),
    ('GM', 'Group Member'),
    ('RS', 'Request Sent'),
    ('NC','')
)

class User(AbstractUser):
    # id = models.IntegerField(primary_key=True, unique=True, auto_created=True)    

    def __str__(self):
        return self.username

class Groups(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, auto_created=True)
    group_name = models.CharField(max_length=100, null=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="user_1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_2")
    user3 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_3")
    user4 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_4")

class Invitation(models.Model):
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name="group_id")
    email = models.EmailField(primary_key=True)
    user_joined = models.BooleanField(null=True, default=False)



    