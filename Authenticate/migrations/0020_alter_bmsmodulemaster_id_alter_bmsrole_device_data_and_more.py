# Generated by Django 4.1.7 on 2023-05-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0016_alter_bmsaccesscontrolrfidmaster_id_and_more'),
        ('Authenticate', '0019_auto_20230526_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmsmodulemaster',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bmsrole',
            name='device_data',
            field=models.ManyToManyField(blank=True, to='Device.bmsdeviceinformation'),
        ),
        migrations.AlterField(
            model_name='bmsrole',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bmsrole',
            name='modules_permission',
            field=models.ManyToManyField(blank=True, to='Authenticate.bmsmodulemaster'),
        ),
        migrations.AlterField(
            model_name='bmsrole',
            name='role_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bmsrolesdevicesinformation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bmsuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bmsuserhasareaacces',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bmsusersdetail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bmsusertype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bmsuservehiclesdetail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bmsuserwallet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bmsuserwallettransaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]