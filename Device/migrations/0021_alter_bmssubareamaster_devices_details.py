# Generated by Django 4.1.7 on 2023-05-31 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0020_rename_scene_id_bmstriggers_scene_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmssubareamaster',
            name='devices_details',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_used': 'No'}, null=True, to='Device.bmsdeviceinformation'),
        ),
    ]