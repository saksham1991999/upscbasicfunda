# Generated by Django 2.2 on 2020-08-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_usercart_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='single_product',
            field=models.BooleanField(default=False),
        ),
    ]
