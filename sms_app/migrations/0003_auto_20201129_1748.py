# Generated by Django 3.1.3 on 2020-11-29 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0002_auto_20201129_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to='student_photo/'),
        ),
    ]
