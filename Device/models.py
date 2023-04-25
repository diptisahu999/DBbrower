from django.db import models
from django.utils import timezone


# from Authodication.models import Bms_Users,Bms_Module_master



# Create your models here
class bms_building_master(models.Model):
    tower_name=models.CharField(max_length=100)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tower_name
    
class bms_floor_master(models.Model):
    tower_id=models.ManyToManyField(bms_building_master)
    floor_name=models.CharField(max_length=100)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.floor_name
    
    
class bms_department_master(models.Model):
    department_name=models.CharField(max_length=100)
    floor_id=models.ManyToManyField(bms_floor_master,blank=True)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.department_name
    
    
class bms_area_master(models.Model):
    area_name=models.CharField(max_length=100)
    floor_id=models.ManyToManyField(bms_floor_master,blank=True)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.area_name
    
    class Meta():
        db_table='bms_area_master_tbl'  
    
class bms_sub_area_master(models.Model):
    
    sub_area_name=models.CharField(max_length=100)
    # department_id=models.ManyToManyField(bms_department_master, blank=True)
    area_id=models.ManyToManyField(bms_area_master,blank=True)
    on_image_path = models.CharField(max_length=255,blank=True)
    off_image_path = models.CharField(max_length=255,blank=True)
    width = models.CharField(max_length=100,blank=True)
    height = models.CharField(max_length=100,blank=True)
    seating_capacity=models.BigIntegerField()
    devices_details = models.JSONField(default=dict, null=True, blank=True)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sub_area_name
    
    class Meta():
        db_table='bms_sub_area_master_tbl'  
    
    
    
class bms_locker(models.Model):
    CATEGORIES=[
        ("Normal","Normal"),
        ("Big","Big"),
    ]
    
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    
    locker_name=models.CharField(max_length=100)
    sub_area_id=models.ManyToManyField(bms_sub_area_master, blank=True)
    category=models.CharField(max_length=100,choices=CATEGORIES)
    status=models.CharField(max_length=100, choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.locker_name
    
class bms_access_control_rfid_master(models.Model):
    CARD_TYPES=[
        ('No-assign','No-assign'),
        ('Static','Static'),
        ('Dynamic','Dynamic')
    ]
    
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    
    rfid_no=models.IntegerField()
    user_id=models.ManyToManyField(to='Authenticate.Bms_Users')
    # user_id=models.ManyToManyField(Bms_Users,blank=True)
    card_type=models.CharField(max_length=100, choices=CARD_TYPES)
    access_area_id=models.ManyToManyField(bms_sub_area_master,blank=True)
    status=models.CharField(max_length=100, choices=STATUS)
    access_start_time=models.DateField(default=timezone.now)
    access_end_time=models.DateField(default=timezone.now)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.rfid_no)
    

class bms_history(models.Model):
    TYPES=[
        ('Newuser','Newuser'),
        ('Visitor','Visitor'),
        ('Access','Access'),
        ('Conference','Conference'),
    ]
    
    user_id=models.ManyToManyField(to='Authenticate.Bms_Users', blank=True)
    # user_id=models.ManyToManyField(Bms_Users, blank=True)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    type=models.CharField(max_length=100, choices=TYPES)
    description=models.JSONField(default=dict, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.type
    

class bms_settings(models.Model):
    module_id=models.ManyToManyField(to='Authenticate.Bms_Module_master',blank=True)
    # module_id=models.ManyToManyField(Bms_Module_master,blank=True)
    setting_data=models.JSONField(default=dict, null=True, blank=True)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
class bms_hardware_type_master(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name=models.CharField(max_length=12,blank=False, null=False)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta():
        db_table='bms_hardware_tbl'
        
        
class bms_device_type_master(models.Model):
    hardware_type_id=models.ManyToManyField(bms_hardware_type_master)
    name=models.CharField(max_length=12)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta():
        db_table='bms_device_tbl'
        
        
class bms_device_information(models.Model):
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    # hardware_type_id=models.ManyToManyField(Bms_hardware_type,related_name='device')
    device_type=models.ManyToManyField(bms_device_type_master,blank=True)
    devices_details = models.ManyToManyField(bms_sub_area_master, blank=True)
    device_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    device_informations=models.JSONField(default=dict, null=True, blank=True)
    status = models.CharField(max_length=100,default=False,choices=STATUS)
    is_used=models.CharField(max_length=100,choices=STATUS)
    create_at=models.DateTimeField(default=timezone.now)
    updated_user_details_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_name
    
    class Meta():
        db_table='bms_device_master_tbl'
        
        
class Bms_device_status_history(models.Model):
    device_id=models.ManyToManyField(bms_sub_area_master,related_name='device_id')
    status = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return self.device_name
    
    class Meta():
        db_table='bms_device_status_tbl'


class bms_user_area_cards_List(models.Model):
    user_id=models.ManyToManyField(to='Authenticate.Bms_Users', blank=True)
    card_id=models.IntegerField()
    card_type=models.CharField(max_length=100,blank=True)
    card_name=models.CharField(max_length=100,blank=True)
    devices_details = models.JSONField(default=dict, null=True, blank=True)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_at=models.DateTimeField(default=timezone.now)
    department_id=models.ManyToManyField(bms_department_master,blank=True)
    # floor_id=models.ManyToManyRel(Bms_floor_master)
    status = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return self.device_name
    
    class Meta():
        db_table='bms_user_area_cards_list_tbl'

