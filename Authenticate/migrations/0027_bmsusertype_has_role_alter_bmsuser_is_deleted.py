# Generated by Django 4.1.7 on 2023-06-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authenticate', '0026_alter_bmsuser_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmsusertype',
            name='has_role',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=23),
        ),
        migrations.AlterField(
            model_name='bmsuser',
            name='is_deleted',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=23),
        ),
    ]