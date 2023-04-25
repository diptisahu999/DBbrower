from django.db import models
from django.utils import timezone
from Device.models import bms_department_master,bms_locker


# Create your models here.

class Bms_Module_master(models.Model):
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    
    module_name=models.CharField(max_length=254)
    module_slug=models.CharField(max_length=254)
    status = models.CharField(max_length=100,choices=STATUS,blank=True)
    created_module_date=models.DateTimeField(default=timezone.now)
    updated_module_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.module_name
    
    class Meta():
        db_table='bms_module_tbl'
        
        
class Bms_Roles(models.Model):
    permissions_id=models.ManyToManyField(Bms_Module_master,related_name='dev')
    role_name=models.CharField(max_length=100)
    device_information= models.JSONField(default=dict, null=True, blank=True)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_role_date=models.DateTimeField(default=timezone.now)
    updated_role_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.role_name
    
    class Meta():
        db_table='bms_role_tbl'
  
  
        
class Bms_User_Type(models.Model):
    # STATUS= [
    #     ("A","Admin"),
    #     ("E","Employee"),
    #     ("M","Manager"),
    #     ("V","Visitor"),
        
    # ]
    # user_type_name=models.CharField(max_length=23,choices=STATUS)
    # user_type_name=models.CharField(max_length=12)
    type_name=models.ManyToManyField(Bms_Roles,blank=True,related_name='aaa')
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_user_type_date=models.DateTimeField(default=timezone.now)
    
    
    class Meta():
        db_table='bms_user_type_tbl'
        
        
            
class Bms_Users_Details(models.Model):
    # from Device.models import Bms_department_master,Bms_locker
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    # user_id=models.ManyToManyField(Bms_Users,related_name='abc')
    # role_id=models.ManyToManyField(Bms_Roles,blank=True,related_name='xyz')
    # department_id=models.ManyToManyField(bms_department_master,related_name='dep')
    # locker_id=models.ManyToManyField(bms_locker,related_name='locker')
    first_name=models.CharField(max_length=254)
    last_name=models.CharField(max_length=254)
    image=models.ImageField(upload_to ='uploads/', blank=True)
    phone_no=models.CharField(max_length=16)
    birthday=models.DateField(auto_now_add=True)
    address=models.TextField(max_length=2321)
    status = models.CharField(max_length=100,choices=STATUS)
    created_user_details_date=models.DateTimeField(default=timezone.now)
    updated_user_details_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name
    class Meta():
        db_table='bms_user_details_tbl'
        
        
        
class Bms_Users(models.Model):
    # user_type=models.ManyToManyField(Bms_User_Type,related_name='use')
    user_details=models.ManyToManyField(Bms_Users_Details,related_name='abc')
    role_id=models.ManyToManyField(Bms_Roles,blank=True,related_name='song')
    user_email=models.EmailField()
    user_password=models.CharField(max_length=254)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    status = models.BooleanField(default=False)
    created_user_date=models.DateTimeField(default=timezone.now)
    updated_user_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user_email
    class Meta():
        db_table='bms_user_tbl'
        
        
        
# user added table

class Bms_Users_register(models.Model):
    
    department_id=models.ManyToManyField(bms_department_master)
    locker_id=models.ManyToManyField(bms_locker)
    first_name=models.CharField(max_length=254)
    last_name=models.CharField(max_length=254)
    phone_no=models.CharField(max_length=16)
    birthday=models.DateField(auto_now_add=True)
    address=models.TextField(max_length=2321)
    STATUS= [
        ("Active","Active"),
        ("In-Active","In-Active"),
    ]
    status = models.CharField(max_length=100,choices=STATUS, blank=True)
    created_user_details_date=models.DateTimeField(default=timezone.now)
    updated_user_details_date=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.first_name
    class Meta():
        db_table='bms_user_register_tbl'
        
        
    