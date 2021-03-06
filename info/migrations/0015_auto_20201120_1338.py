# Generated by Django 3.1.3 on 2020-11-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0014_auto_20201119_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigntime',
            name='day',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday')], max_length=15),
        ),
        migrations.AlterField(
            model_name='assigntime',
            name='period',
            field=models.CharField(choices=[('1st', '8:30 - 9:25'), ('2nd', '9:25 - 10:20'), ('3rd', '10:40 - 11:35'), ('4th', '11:35 - 12:30'), ('5th', '12:30 - 1:25'), ('6th', '1:45 - 2:40'), ('7th', '2:40 - 3:35'), ('8th', '3:35 - 4:30'), ('9th', '4:30 - 5:25'), ('10th', '5:25 - 6:20')], default='11:00 - 11:50', max_length=50),
        ),
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('Mt 1', 'Mid-term 1'), ('Mt 2', 'Mid-term 2'), ('TA', 'Teacher Asessment'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('Mt 1', 'Mid-term 1'), ('Mt 2', 'Mid-term 2'), ('TA', 'Teacher Asessment'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Male', max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Male', max_length=50),
        ),
    ]
