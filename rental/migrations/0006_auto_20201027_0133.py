# Generated by Django 2.2 on 2020-10-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_auto_20201027_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationdate',
            name='date',
            field=models.DateField(null=True, unique=True),
        ),
    ]
