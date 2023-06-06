# Generated by Django 4.1.7 on 2023-06-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0026_bmssceneappliancesdetails_componet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmsareamaster',
            name='is_deleted',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23),
        ),
        migrations.AlterField(
            model_name='bmsbuildingmaster',
            name='is_deleted',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23),
        ),
        migrations.AlterField(
            model_name='bmsfloormaster',
            name='is_deleted',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23),
        ),
        migrations.AlterField(
            model_name='bmssceneappliancesdetails',
            name='is_deleted',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23),
        ),
        migrations.AlterField(
            model_name='bmsscenes',
            name='is_deleted',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23),
        ),
        migrations.AlterField(
            model_name='bmssubareamaster',
            name='is_deleted',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23),
        ),
        migrations.AlterField(
            model_name='bmstriggers',
            name='is_deleted',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23),
        ),
    ]