# Generated by Django 3.2.18 on 2023-05-03 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_id_alter_user_partnerid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='invite_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='partnerId',
        ),
        migrations.RemoveField(
            model_name='user',
            name='request_sent',
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('group_name', models.CharField(max_length=100, null=True)),
                ('request_sent', models.BooleanField(default=False)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_2', to=settings.AUTH_USER_MODEL)),
                ('user3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_3', to=settings.AUTH_USER_MODEL)),
                ('user4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_4', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]