# Generated by Django 3.0.4 on 2020-05-05 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='items',
        ),
    ]
