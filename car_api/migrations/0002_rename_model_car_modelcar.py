# Generated by Django 3.2.7 on 2021-09-05 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='model',
            new_name='modelCar',
        ),
    ]
