# Generated by Django 2.2 on 2020-10-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0017_auto_20201028_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(null=True, upload_to='AirbnbProject/images'),
        ),
    ]