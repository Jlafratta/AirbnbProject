# Generated by Django 2.2 on 2020-10-27 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20201027_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='property',
        ),
    ]
