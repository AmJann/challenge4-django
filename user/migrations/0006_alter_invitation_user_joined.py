# Generated by Django 3.2.18 on 2023-05-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20230505_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='user_joined',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
