from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)    

    def __str__(self):
        return self.username

class Groups(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, auto_created=True)
    group_name = models.CharField(max_length=100, null=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="user_1")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_2")
    user3 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_3")
    user4 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_4")
    request_sent = models.BooleanField(default=False)

    