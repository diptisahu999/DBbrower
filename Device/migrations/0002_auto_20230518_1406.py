# Generated by Django 3.1.5 on 2023-05-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmsuserareacardslist',
            name='devices_details',
        ),
        migrations.AddField(
            model_name='bmsuserareacardslist',
            name='devices_details',
            field=models.ManyToManyField(blank=True, null=True, to='Device.BmsDeviceInformation'),
        ),
    ]
