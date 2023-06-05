# Generated by Django 3.1.5 on 2023-05-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authenticate', '0006_auto_20230517_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmsrole',
            name='permissions_id',
        ),
        migrations.RemoveField(
            model_name='bmsusertype',
            name='user_type_name',
        ),
        migrations.AddField(
            model_name='bmsrole',
            name='modules_id',
            field=models.ManyToManyField(to='Authenticate.BmsModuleMaster'),
        ),
        migrations.AlterField(
            model_name='bmsrole',
            name='role_name',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Employee', 'Employee'), ('Manager', 'Manager'), ('Visitor', 'Visitor')], max_length=100),
        ),
    ]