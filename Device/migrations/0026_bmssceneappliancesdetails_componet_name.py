# Generated by Django 4.1.7 on 2023-06-06 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0025_merge_20230606_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmssceneappliancesdetails',
            name='componet_name',
            field=models.CharField(default=True, max_length=23),
        ),
    ]