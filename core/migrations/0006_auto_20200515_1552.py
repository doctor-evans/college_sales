# Generated by Django 3.0.4 on 2020-05-15 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200505_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bought',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
