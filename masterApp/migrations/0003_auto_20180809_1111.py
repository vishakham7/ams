# Generated by Django 2.1 on 2018-08-09 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterApp', '0002_auto_20180809_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidays',
            name='date',
            field=models.CharField(default=datetime.datetime(2018, 8, 9, 11, 11, 40, 81568), max_length=100),
        ),
    ]