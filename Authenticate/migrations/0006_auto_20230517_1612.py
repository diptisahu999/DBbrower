# Generated by Django 3.1.5 on 2023-05-17 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0001_initial'),
        ('Authenticate', '0005_remove_bmsrolesdevicesinformation_updatated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmsrolesdevicesinformation',
            name='subarea_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Device.bmssubareamaster'),
        ),
    ]
