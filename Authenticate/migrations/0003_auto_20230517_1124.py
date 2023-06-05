# Generated by Django 3.1.5 on 2023-05-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0001_initial'),
        ('Authenticate', '0002_auto_20230513_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmsrole',
            name='device_information',
        ),
        migrations.RemoveField(
            model_name='bmsrolesdevicesinformation',
            name='device_information_id',
        ),
        migrations.AddField(
            model_name='bmsrolesdevicesinformation',
            name='device_information_id',
            field=models.ManyToManyField(to='Device.BmsDeviceInformation'),
        ),
        migrations.DeleteModel(
            name='BmsRolesDeviceInformation',
        ),
    ]