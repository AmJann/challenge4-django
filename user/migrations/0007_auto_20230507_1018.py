# Generated by Django 3.2.18 on 2023-05-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_invitation_user_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='id',
        ),
        migrations.AlterField(
            model_name='invitation',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
