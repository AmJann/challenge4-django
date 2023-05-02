# Generated by Django 4.2 on 2023-05-02 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='partnerId',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_partners', to=settings.AUTH_USER_MODEL),
        ),
    ]
