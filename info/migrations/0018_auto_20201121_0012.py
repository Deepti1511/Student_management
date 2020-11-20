# Generated by Django 3.1.3 on 2020-11-20 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0017_auto_20201120_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Room',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date(2020, 11, 21)),
        ),
    ]
