from django.utils import timezone
from django.db import models



# Create your models here
class BmsBuildingMaster(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    DELETE=[
        ("No","No"),
        ("Yes","Yes")
    ]
    tower_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    is_deleted=models.CharField(max_length=23,choices=DELETE,default=DELETE[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tower_name

    class Meta():
        db_table = 'bms_building_master'


class BmsFloorMaster(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    
    DELETE=[
        ("No","No"),
        ("Yes","Yes")
    ]
    tower_data = models.ForeignKey(BmsBuildingMaster,on_delete=models.CASCADE,related_name='floor_data',null=True,blank=True)   ## changeses
    floor_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    is_deleted=models.CharField(max_length=23,choices=DELETE,default=DELETE[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.floor_name

    class Meta():
        db_table = 'bms_floor_master'


class BmsAreaMaster(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    
    DELETE=[
        ("No","No"),
        ("Yes","Yes")
    ]
    area_name = models.CharField(max_length=100)
    floor_data = models.ForeignKey(BmsFloorMaster,on_delete=models.CASCADE,related_name='areas_data',null=True,blank=True)
    status = models.CharField(max_length=100, choices=STATUS,default=STATUS[0][0])
    is_deleted=models.CharField(max_length=23,choices=DELETE,default=DELETE[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.area_name

    class Meta():
        db_table = 'bms_area_master '
        
        
        

class BmsDeviceInformation(models.Model):
    device_slug = [("LED","LED"),
                   ("AC","AC"),
                   ("TV","TV"),
                   ("CURTAIN","CURTAIN"),
                   ("PROJECTOR","PROJECTOR"),
                   ("AVR","AVR"),
                   ("MP","MP"),
                   ("BRP","BRP"),
                   ("STB","STB"),
                   ("CAMERA","CAMERA"),
                   ("SPEAKER","SPEAKER")
                    ]

    is_used_STATUS = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    device_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100 ,choices=device_slug,blank=True)
    is_used = models.CharField(
        max_length=23, choices=is_used_STATUS, default=is_used_STATUS[1][1])
    device_informations = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    create_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_user_details_date = models.DateTimeField(auto_now=True)
    # devices_details = models.ForeignKey(bms_sub_area_master,on_delete=models.CASCADE,related_name='device_data')
    # hardware_type_id=models.ForeignKey(Bms_hardware_type,on_delete=models.CASCADE,related_name='device')
    
    
    def __str__(self):
        return self.device_name

    class Meta():
        db_table = 'bms_device_information'


class BmsDepartmentMaster(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    department_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS,default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department_name

    class Meta():
        db_table = 'bms_department_master'


class BmsSubAreaMaster(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    DELETE=[
        ("No","No"),
        ("Yes","Yes")
    ]
    # floor_id=models.ForeignKey(bms_floor_master,on_delete=models.CASCADE)
    # tower_details=models.ForeignKey(bms_building_master,on_delete=models.CASCADE)
    sub_area_name = models.CharField(max_length=100)
    area_data = models.ForeignKey(BmsAreaMaster,on_delete=models.CASCADE,related_name='sub_areas_data',null=True,blank=True)
    on_image_path = models.CharField(max_length=255, blank=True)
    off_image_path = models.CharField(max_length=255, blank=True)
    width = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=100, blank=True)
    seating_capacity = models.BigIntegerField()
    devices_details = models.ManyToManyField(BmsDeviceInformation,limit_choices_to={'is_used': 'No'},blank=True)
    status = models.CharField(max_length=100, choices=STATUS,default=STATUS[0][0])
    is_deleted=models.CharField(max_length=23,choices=DELETE,default=DELETE[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_area_name

    class Meta():
        db_table = 'bms_sub_area_master'


class BmsLocker(models.Model):
    CATEGORIES = [
        ("Normal", "Normal"),
        ("Big", "Big"),
    ]

    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    category = models.CharField(max_length=100, choices=CATEGORIES)
    sub_area_data = models.ForeignKey(BmsSubAreaMaster,on_delete=models.CASCADE)
    locker_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.locker_name

    class Meta():
        db_table = 'bms_locker'


class BmsAccessControlRfidMaster(models.Model):
    CARD_TYPES = [
        ('No-assign', 'No-assign'),
        ('Static', 'Static'),
        ('Dynamic', 'Dynamic')
    ]

    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    user_data = models.ForeignKey(to='Authenticate.BmsUser',on_delete=models.CASCADE)
    rfid_no = models.IntegerField()
    card_type = models.CharField(max_length=100, choices=CARD_TYPES)
    access_area_data = models.ForeignKey(BmsSubAreaMaster,on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    access_start_time = models.DateField(default=timezone.now)
    access_end_time = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rfid_no)

    class Meta():
        db_table = 'bms_access_control_rfid_master'


class BmsHistory(models.Model):
    TYPES = [
        ('Newuser', 'Newuser'),
        ('Visitor', 'Visitor'),
        ('Access', 'Access'),
        ('Conference', 'Conference'),
    ]
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    user_data = models.ForeignKey(to='Authenticate.BmsUser',on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=TYPES)
    description = models.JSONField(default=dict, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

    class Meta():
        db_table = 'bms_history'


class BmsSettings(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    module_data = models.ForeignKey(to='Authenticate.BmsModuleMaster',on_delete=models.CASCADE)
    setting_data = models.JSONField(default=dict, null=True)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.setting_data

    class Meta():
        db_table = 'bms_settings'


class BmsHardwareTypeMaster(models.Model):
    Hardware_choice = [
        ("Relay", "Relay"),
        ("Dali", "Dali"),
        ("CoolMaster", "CoolMaster"),
    ]
    
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    id = models.AutoField(primary_key=True, unique=True)
    hardware_name = models.CharField(
        max_length=12, choices=Hardware_choice, blank=True, null=False)
    status = models.CharField(max_length=100, choices=STATUS,default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hardware_name

    class Meta():
        db_table = 'bms_hardware_type_master'

class BmsDeviceTypeMaster(models.Model):
    device_slug = [("LED","LED"),
                   ("AC","AC"),
                   ("TV","TV"),
                   ("CURTAIN","CURTAIN"),
                   ("PROJECTOR","PROJECTOR"),
                   ("AVR","AVR"),
                   ("MP","MP"),
                   ("BRP","BRP"),
                   ("STB","STB"),
                   ("CAMERA","CAMERA"),
                   ("SPEAKER","SPEAKER")
                   ]
    
    
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    
    hardware_type_data = models.ForeignKey(BmsHardwareTypeMaster,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    device_type_slug = models.CharField(max_length=100,choices=device_slug)
    status = models.CharField(max_length=100, choices=STATUS,default=STATUS[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.name

    class Meta():
        db_table = 'bms_device_type_master'
        
        
    

class BmsDeviceStatusHistory(models.Model):
    device_data = models.ForeignKey(BmsSubAreaMaster,on_delete=models.CASCADE)
    device_status = models.BooleanField(default=False)
    user_data = models.ForeignKey(to='Authenticate.BmsUser',on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.device_data)

    class Meta():
        db_table = 'bms_device_status_history'


class BmsUserAreaCardsList(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    user_data = models.ForeignKey(to='Authenticate.BmsUser',on_delete=models.CASCADE)
    card_id = models.IntegerField()
    column_no = models.IntegerField(default=1)
    user_card_name = models.CharField(max_length=100, blank=True)
    card_title = models.CharField(max_length=100, blank=True)
    device_details = models.ManyToManyField(BmsDeviceInformation,blank=True)
    card_slug = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    created_at = models.DateTimeField(default=timezone.now)
    # floor_id=models.ForeignKey(Bms_floor_master,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user_card_name

    class Meta():
        db_table = 'bms_user_area_cards_list'





class BmsScenes(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    
    OPERATION=[
        ("on", "on"),
        ("off", "off"),
    ]
    DELETE=[
        ("No","No"),
        ("Yes","Yes")
    ]
    
    
    scene_name =models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    is_deleted=models.CharField(max_length=23,choices=DELETE,default=DELETE[0][0])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.scene_name

    class Meta():
        db_table = 'bms_scenes'



class BmsSceneAppliancesDetails(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    DELETE=[
        ("No","No"),
        ("Yes","Yes")
    ]
    scene=models.ForeignKey(BmsScenes,on_delete=models.CASCADE,related_name='scene_appliance_details')
    device_type_slug=models.CharField(max_length=23,blank=True)
    component_id=models.ForeignKey(BmsDeviceInformation,on_delete=models.CASCADE)
    componet_name= models.CharField(max_length=23,default=True)
    operation_type=models.CharField(max_length=23,blank=True)
    operation_value=models.CharField(max_length=23,blank=True)
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    is_deleted=models.CharField(max_length=23,choices=DELETE,default=DELETE[0][0])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.id)

    class Meta():
        db_table = 'bms_scene_appliances_details'
        

class BmsTriggers(models.Model):
    STATUS = [
        ("Active", "Active"),
        ("In-Active", "In-Active"),
    ]
    action_type_choice = [
        ("Event", "Event"),
        ("Schedule", "Schedule"),
    ]
    DELETE=[
        ("No","No"),
        ("Yes","Yes")
    ]
    

    trigger_name = models.CharField(max_length=100, blank=True)
    action_type = models.CharField(max_length=100, choices=action_type_choice,blank=True)
    trigger_data =models.JSONField()
    status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
    is_deleted=models.CharField(max_length=23,choices=DELETE,default=DELETE[0][0])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trigger_name

    class Meta():
        db_table = 'bms_triggers'
