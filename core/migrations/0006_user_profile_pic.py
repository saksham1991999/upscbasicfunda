# Generated by Django 2.2 on 2020-08-05 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_usersubscriptions_tests'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]