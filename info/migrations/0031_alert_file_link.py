# Generated by Django 2.2.17 on 2020-11-22 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0030_alert'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='File_link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
