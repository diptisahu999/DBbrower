# Generated by Django 3.1.5 on 2023-05-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0002_auto_20230518_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmsuserareacardslist',
            name='devices_details',
            field=models.ManyToManyField(blank=True, to='Device.BmsDeviceInformation'),
        ),
    ]
