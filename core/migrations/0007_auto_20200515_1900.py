# Generated by Django 3.0.4 on 2020-05-15 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200515_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='date',
            new_name='date_added',
        ),
    ]
