# Generated by Django 2.2.13 on 2021-05-31 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_auto_20210520_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_verified',
        ),
    ]
