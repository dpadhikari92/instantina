# Generated by Django 3.0.7 on 2023-05-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20230523_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bomrawmaterial',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='production',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
