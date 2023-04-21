from rest_framework import serializers 

from Device.models import *


#GET Building
class Bms_Bulding_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=bms_building_master
        fields='__all__'
        
#GET Floor
class Bms_floor_serializer(serializers.ModelSerializer):
    class Meta:
        tower_id = Bms_Bulding_master_Serializer(many=True, read_only=True)
        model = bms_floor_master
        fields = '__all__'
        depth = 10

#post Floor
class Bms_floor_master_Serializer_post(serializers.ModelSerializer):
    class Meta:
        model=bms_floor_master
        fields='__all__'
        

        
#GET  Department
class Bms_department_master_Serializer(serializers.ModelSerializer):
    floor_id=Bms_floor_serializer(many=True,read_only=True)
    class Meta:
        model=bms_department_master
        fields='__all__'
        depth = 10

#post Department
class Bms_department_master_Serializer_post(serializers.ModelSerializer):
    class Meta:
        model=bms_department_master
        fields='__all__'
        



#GET area     
class bms_area_Serializer(serializers.ModelSerializer):

    class Meta:
        # tower_id = Bms_Bulding_master_Serializer(many=True, read_only=True)
        # floor_id=Bms_floor_serializer(many=True,read_only=True)
        model= bms_area_master
        fields='__all__'
        depth = 10

#post area  
class bms_area_Serializer_post(serializers.ModelSerializer):
    class Meta:
        model= bms_area_master
        fields='__all__'
        

#GET Sub_area
class Bms_sub_area_master_Serializer(serializers.ModelSerializer):
    floor_id=Bms_floor_serializer(many=True,read_only=True)
    area_id =bms_area_Serializer(many=True,read_only=True)
    class Meta:
        model=bms_sub_area_master
        fields='__all__'
        depth = 10
        

#post Sub_area
class Bms_sub_area_master_Serializer_post(serializers.ModelSerializer):
    class Meta:
        model=bms_sub_area_master
        fields='__all__'


#GET Locker
class Bms_locker_Serializer(serializers.ModelSerializer):
    sub_area_id =Bms_sub_area_master_Serializer(many=True,read_only=True)
    class Meta:
        model=bms_locker
        fields='__all__'
        depth = 10
#post Locker        
class Bms_locker_Serializer_post(serializers.ModelSerializer):
    class Meta:
        model=bms_locker
        fields='__all__'

#GET
class Bms_hardware_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model= bms_hardware_type_master
        fields='__all__'
        depth = 10



#GET Device Type
class Bms_device_type_Serializer(serializers.ModelSerializer):
    hardware_type_id = Bms_hardware_type_Serializer(many=True,read_only=True)
    class Meta:
        model= bms_device_type_master
        fields='__all__'
        depth = 10



#Post Device type
class Bms_device_type_Serializer_post(serializers.ModelSerializer):
    class Meta:
        model= bms_device_type_master
        fields='__all__'



#GET Device informations
class Bms_Devices_Serializer(serializers.ModelSerializer):
    device_type = Bms_device_type_Serializer(many=True,read_only=True)
    hardware_type_id = Bms_hardware_type_Serializer(many=True,read_only=True)
    class Meta:
        model= bms_device_information
        fields='__all__'
        depth = 10
#post Device Informations
class Bms_Devices_Serializer_post(serializers.ModelSerializer):
    class Meta:
        model= bms_device_information
        fields='__all__'




#GET
class Bms_device_status_history_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Bms_device_status_history
        fields='__all__'
        depth = 10

    

        
#GET
class Bms_user_area_cards_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model= bms_user_area_cards_List
        fields='__all__'
        depth = 10




#GET
class bms_building_floor_area_subarea_device_Serializer(serializers.ModelSerializer):
    class Meta:
        floor=Bms_floor_serializer(many=True,read_only=True)
        area=Bms_sub_area_master_Serializer(many=True,read_only=True)
        subarea =Bms_sub_area_master_Serializer(many=True,read_only=True)
        building =Bms_Bulding_master_Serializer(many=True,read_only=True)
        device =Bms_Devices_Serializer(many=True,read_only=True)


    class Meta:
        model = bms_sub_area_master
        fields = '__all__'
        depth = 10





#GET
class bms_user_area_cards_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model= bms_user_area_cards_List
        fields='__all__'
        depth = 10
