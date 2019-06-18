# Generated by Django 2.1.7 on 2019-06-17 12:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 17, 12, 58, 28, 978054)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Address', verbose_name='restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='restaurants.Category', verbose_name='ca_restaurant_list'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, to='restaurants.Comment', verbose_name='co_restaurant_list'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='foods',
            field=models.ManyToManyField(blank=True, null=True, to='restaurants.Food', verbose_name='fo_restaurant_list'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]