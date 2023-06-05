# Generated by Django 4.1.7 on 2023-05-25 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authenticate', '0014_remove_bmsrolesdevicesinformation_subarea_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmsuser',
            name='role_id',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='bms_role', to='Authenticate.bmsrole'),
        ),
        migrations.AlterField(
            model_name='bmsuser',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100),
        ),
    ]
