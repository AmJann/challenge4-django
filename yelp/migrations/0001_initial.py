# Generated by Django 3.2.18 on 2023-05-03 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_auto_20230503_1737'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=50, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.groups')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resturant_id', models.CharField(max_length=30)),
                ('resturant_categories', models.CharField(max_length=500)),
                ('resturant_distance', models.DecimalField(decimal_places=6, max_digits=9)),
                ('resturant_price', models.CharField(max_length=10)),
                ('resturant_rating', models.IntegerField()),
                ('user_rating', models.IntegerField()),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yelp.list')),
            ],
        ),
    ]