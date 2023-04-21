from rest_framework import serializers 
from Authenticate.models import Bms_Module_master,Bms_Roles,Bms_User_Type,Bms_Users,Bms_Users_Details,Bms_Users_register
from Device.models import bms_department_master,bms_locker





class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_Module_master
        fields='__all__'
 
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        permissions_id = ModuleSerializer(many=True,read_only=True)
        model=Bms_Roles
        fields='__all__'
        
class UserTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Bms_User_Type
        fields=['id','user_type_name']        
        
        
class DepertmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=bms_department_master
        fields=['id','department_name'] 
        
class lockerSerializer(serializers.ModelSerializer):
    class Meta:
        model=bms_locker
        fields=['id','locker_name']
         
class BmsUserSerializer(serializers.ModelSerializer):
    # user_type_id=UserTypeSerializer(many=True,read_only=True)

    class Meta:
        role_id=RoleSerializer(many=True,read_only=True)
        department_id=DepertmentSerializer(many=True,read_only=True)
        locker_id=lockerSerializer(many=True,read_only=True)
        model = Bms_Users_Details
        fields = '__all__'
        
class BmsUserDetailsSerializer(serializers.ModelSerializer):

    
    class Meta:
        role_id=RoleSerializer(many=True,read_only=True)
        user_details=BmsUserSerializer(many=True,read_only=True)
        department_id=DepertmentSerializer(many=True,read_only=True)
        locker_id=lockerSerializer(many=True,read_only=True)
        model = Bms_Users
        fields = '__all__'
        
        

# user registation        
        
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        department_id=DepertmentSerializer(many=True,read_only=True)
        locker_id=lockerSerializer(many=True,read_only=True)
        model = Bms_Users_Details
        fields = '__all__'
        
        
        
#user Views
class Manage_user_view(serializers.ModelSerializer):
    class Meta:
        model = '__all__'