# Generated by Django 3.1.5 on 2023-05-18 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0003_auto_20230518_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bmsuserareacardslist',
            old_name='card_name',
            new_name='user_card_name',
        ),
    ]