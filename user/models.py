from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    request_sent = models.BooleanField(default=False)
    invite_code = models.UUIDField(editable=True, unique=False,auto_created=True, default=uuid.uuid4)
    partnerId = models.ForeignKey('self', on_delete=models.CASCADE,unique=False, default=None, null=True, related_name='user_partners')
    

    def __str__(self):
        return self.username

