# Generated by Django 3.2 on 2021-05-09 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0009_auto_20210509_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_date',
            field=models.CharField(default=datetime.date(2021, 5, 9), max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_time',
            field=models.CharField(default=datetime.time(13, 29, 43, 170919), max_length=100, null=True),
        ),
    ]
