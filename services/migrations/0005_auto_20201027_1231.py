# Generated by Django 2.2 on 2020-10-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_remove_service_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]