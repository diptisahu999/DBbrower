# Generated by Django 3.1.5 on 2023-05-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0006_auto_20230518_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmssubareamaster',
            name='devices_details',
            field=models.ManyToManyField(limit_choices_to={'is_used': False}, to='Device.BmsDeviceInformation'),
        ),
    ]
