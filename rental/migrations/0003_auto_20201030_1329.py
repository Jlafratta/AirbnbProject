# Generated by Django 2.2 on 2020-10-30 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_auto_20201030_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='code',
            field=models.CharField(default='', max_length=16),
        ),
    ]
