# Generated by Django 3.0.4 on 2020-05-05 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item_owner'),
        ('users', '0002_remove_profile_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='items',
            field=models.ManyToManyField(to='core.Item'),
        ),
    ]
