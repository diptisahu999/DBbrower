# Generated by Django 4.1.7 on 2023-06-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authenticate', '0022_rename_birthday_bmsusersdetail_dob_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bmsusersdetail',
            name='department_data',
        ),
        migrations.RemoveField(
            model_name='bmsusertype',
            name='role_data',
        ),
        migrations.AddField(
            model_name='bmsusertype',
            name='user_type_name',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Employee', 'Employee'), ('Manager', 'Manager'), ('Visitor', 'Visitor')], default=True, max_length=23),
        ),
    ]
