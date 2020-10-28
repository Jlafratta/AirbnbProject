# Generated by Django 2.2 on 2020-10-28 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0022_auto_20201028_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(null=True, upload_to='properties'),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rental.Property'),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='short_description',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
    ]