# Generated by Django 2.1.7 on 2019-06-27 23:19

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('address_line', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('quality', models.FloatField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('packaging', models.FloatField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('delivery_time', models.FloatField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 6, 27, 23, 19, 15, 609867))),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField()),
                ('food_set', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Address', verbose_name='restaurant')),
                ('categories', models.ManyToManyField(blank=True, null=True, related_name='ca_restaurant_list', to='restaurants.Category')),
                ('comments', models.ManyToManyField(blank=True, null=True, related_name='co_restaurant_list', to='restaurants.Comment')),
                ('foods', models.ManyToManyField(blank=True, null=True, related_name='fo_restaurant_list', to='restaurants.Food')),
            ],
        ),
    ]
