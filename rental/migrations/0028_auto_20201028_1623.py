# Generated by Django 2.2 on 2020-10-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0027_auto_20201028_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(max_length=450),
        ),
    ]
