# Generated by Django 2.2 on 2020-09-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200929_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalnotification',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
