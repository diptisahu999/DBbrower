# Generated by Django 3.1.5 on 2023-06-09 10:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authenticate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BmsAreaMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bms_area_master ',
            },
        ),
        migrations.CreateModel(
            name='BmsBuildingMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tower_name', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bms_building_master',
            },
        ),
        migrations.CreateModel(
            name='BmsDepartmentMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bms_department_master',
            },
        ),
        migrations.CreateModel(
            name='BmsDeviceInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
                ('device_type', models.CharField(blank=True, choices=[('LED', 'LED'), ('AC', 'AC'), ('TV', 'TV'), ('CURTAIN', 'CURTAIN'), ('PROJECTOR', 'PROJECTOR'), ('AVR', 'AVR'), ('MP', 'MP'), ('BRP', 'BRP'), ('STB', 'STB'), ('CAMERA', 'CAMERA'), ('SPEAKER', 'SPEAKER')], max_length=100)),
                ('is_used', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=23)),
                ('device_informations', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('create_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bms_device_information',
            },
        ),
        migrations.CreateModel(
            name='BmsHardwareTypeMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware_type_name', models.CharField(blank=True, choices=[('Relay', 'Relay'), ('Dali', 'Dali'), ('CoolMaster', 'CoolMaster'), ('IR', 'IR'), ('CCTV', 'CCTV')], max_length=12)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bms_hardware_type_master',
            },
        ),
        migrations.CreateModel(
            name='BmsScenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_name', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bms_scenes',
            },
        ),
        migrations.CreateModel(
            name='BmsTriggers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger_name', models.CharField(blank=True, max_length=100)),
                ('action_type', models.CharField(blank=True, choices=[('Event', 'Event'), ('Schedule', 'Schedule')], max_length=100)),
                ('trigger_data', models.JSONField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bms_triggers',
            },
        ),
        migrations.CreateModel(
            name='BmsUserAreaCardsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.IntegerField()),
                ('column_no', models.IntegerField(default=1)),
                ('user_card_name', models.CharField(blank=True, max_length=100)),
                ('card_title', models.CharField(blank=True, max_length=100)),
                ('card_slug', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('device_details', models.ManyToManyField(blank=True, to='Device.BmsDeviceInformation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authenticate.bmsuser')),
            ],
            options={
                'db_table': 'bms_user_area_cards_list',
            },
        ),
        migrations.CreateModel(
            name='BmsSubAreaMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_area_name', models.CharField(blank=True, max_length=100)),
                ('on_image_path', models.CharField(blank=True, max_length=255)),
                ('off_image_path', models.CharField(blank=True, max_length=255)),
                ('width', models.CharField(blank=True, max_length=100)),
                ('height', models.CharField(blank=True, max_length=100)),
                ('seating_capacity', models.BigIntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_areas_data', to='Device.bmsareamaster')),
                ('devices_details', models.ManyToManyField(blank=True, limit_choices_to={'is_used': 'No'}, to='Device.BmsDeviceInformation')),
            ],
            options={
                'db_table': 'bms_sub_area_master',
            },
        ),
        migrations.CreateModel(
            name='BmsSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting_data', models.JSONField(default=dict, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('modules_permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authenticate.bmsmodulemaster')),
            ],
            options={
                'db_table': 'bms_settings',
            },
        ),
        migrations.CreateModel(
            name='BmsSceneAppliancesDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type_slug', models.CharField(blank=True, max_length=23)),
                ('componet_name', models.CharField(default=True, max_length=23)),
                ('operation_type', models.CharField(blank=True, max_length=23)),
                ('operation_value', models.CharField(blank=True, max_length=23)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmsdeviceinformation')),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scene_appliance_details', to='Device.bmsscenes')),
            ],
            options={
                'db_table': 'bms_scene_appliances_details',
            },
        ),
        migrations.CreateModel(
            name='BmsLocker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Normal', 'Normal'), ('Big', 'Big')], max_length=100)),
                ('locker_name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('sub_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmssubareamaster')),
            ],
            options={
                'db_table': 'bms_locker',
            },
        ),
        migrations.CreateModel(
            name='BmsHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Newuser', 'Newuser'), ('Visitor', 'Visitor'), ('Access', 'Access'), ('Conference', 'Conference')], max_length=100)),
                ('description', models.JSONField(blank=True, default=dict, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authenticate.bmsuser')),
            ],
            options={
                'db_table': 'bms_history',
            },
        ),
        migrations.CreateModel(
            name='BmsHardWareDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware_name', models.CharField(blank=True, max_length=23)),
                ('hardware_details', models.JSONField(blank=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=23)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('hardware_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hardware_type_data', to='Device.bmshardwaretypemaster')),
            ],
            options={
                'db_table': 'bms_hardware_details',
            },
        ),
        migrations.CreateModel(
            name='BmsFloorMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_name', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('tower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='floor_data', to='Device.bmsbuildingmaster')),
            ],
            options={
                'db_table': 'bms_floor_master',
            },
        ),
        migrations.CreateModel(
            name='BmsDeviceTypeMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('device_type_slug', models.CharField(choices=[('LED', 'LED'), ('AC', 'AC'), ('TV', 'TV'), ('CURTAIN', 'CURTAIN'), ('PROJECTOR', 'PROJECTOR'), ('AVR', 'AVR'), ('MP', 'MP'), ('BRP', 'BRP'), ('STB', 'STB'), ('CAMERA', 'CAMERA'), ('SPEAKER', 'SPEAKER')], max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('is_deleted', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=23)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('hardware_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmshardwaretypemaster')),
            ],
            options={
                'db_table': 'bms_device_type_master',
            },
        ),
        migrations.CreateModel(
            name='BmsDeviceStatusHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmssubareamaster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authenticate.bmsuser')),
            ],
            options={
                'db_table': 'bms_device_status_history',
            },
        ),
        migrations.AddField(
            model_name='bmsdeviceinformation',
            name='hardware_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmshardwaredetails'),
        ),
        migrations.AddField(
            model_name='bmsareamaster',
            name='floor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='areas_data', to='Device.bmsfloormaster'),
        ),
        migrations.CreateModel(
            name='BmsAccessControlRfidMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid_no', models.IntegerField()),
                ('card_type', models.CharField(choices=[('No-assign', 'No-assign'), ('Static', 'Static'), ('Dynamic', 'Dynamic')], max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-Active', 'In-Active')], default='Active', max_length=100)),
                ('access_start_time', models.DateField(default=django.utils.timezone.now)),
                ('access_end_time', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('access_area_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.bmssubareamaster')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authenticate.bmsuser')),
            ],
            options={
                'db_table': 'bms_access_control_rfid_master',
            },
        ),
    ]
