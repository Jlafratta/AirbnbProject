# Generated by Django 2.2 on 2020-10-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0019_propertyimage_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(null=True, upload_to='AirbnbProject/static/img/properties'),
        ),
    ]
