# Generated by Django 4.1.7 on 2023-06-06 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authenticate', '0023_remove_bmsusersdetail_department_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmsuser',
            name='is_deleted',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=23),
        ),
        migrations.AddField(
            model_name='bmsuserhasareaacces',
            name='is_deleted',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=23),
        ),
        migrations.AddField(
            model_name='bmsusersdetail',
            name='is_deleted',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=23),
        ),
    ]
