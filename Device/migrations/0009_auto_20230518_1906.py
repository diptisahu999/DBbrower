# Generated by Django 3.1.5 on 2023-05-18 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0008_auto_20230518_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bmsdevicetypemaster',
            old_name='hardware_type_id',
            new_name='hardware_type_data',
        ),
        migrations.RenameField(
            model_name='bmsfloormaster',
            old_name='tower_id',
            new_name='tower_data',
        ),
        migrations.RenameField(
            model_name='bmssettings',
            old_name='module_id',
            new_name='module_data',
        ),
    ]
