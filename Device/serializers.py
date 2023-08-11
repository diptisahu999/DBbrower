from rest_framework import serializers
from Device.models import *
from rest_framework.validators import UniqueValidator

# GET Building


class BmsBuildingMasterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=BmsBuildingMaster.objects.all())])
    class Meta:
        model = BmsBuildingMaster
        fields = '__all__'
        depth=10

class BmsBuildingMasterSerializerPost(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=BmsBuildingMaster.objects.all())])
    class Meta:
        model = BmsBuildingMaster
        fields = '__all__'
        # depth=10

# GET Floor

class BmsBuildingMasterSerializer1111(serializers.ModelSerializer):
    class Meta:
        model = BmsBuildingMaster
        fields = ['id','tower_name','created_at','updated_at']
        depth = 10


class BmsFloorMasterSerializer(serializers.ModelSerializer):
    tower_data = BmsBuildingMasterSerializer1111(source='tower', read_only=True)

    class Meta:
        model = BmsFloorMaster
        fields = ['id','floor_name','status','created_at','updated_at','tower_data']
        depth = 10
        

# post Floor


class BmsFloorMasterSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsFloorMaster
        fields ='__all__'
        # depth=10

# GET  Department
class BmsDepartmentMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsDepartmentMaster
        fields ='__all__'
        depth = 10

# post Department


class BmsDepartmentMasterSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsDepartmentMaster
        fields = '__all__'
        depth=10

# GET area
class BmsAreaMasterSerializer(serializers.ModelSerializer):
    floor_data=BmsFloorMasterSerializer(source='floor',read_only=True)
    class Meta:
        model = BmsAreaMaster
        # fields = '__all__'
        fields=['id','area_name','status','created_at','updated_at','floor_data']
        depth = 10



class BmsSubAreaMasterSerializerPut(serializers.ModelSerializer):
    class Meta:
        model = BmsSubAreaMaster
        fields = ['devices_details']
        # depth = 10



    
class SencesSerializersPost(serializers.ModelSerializer):
    class Meta:
        model=BmsScenes
        fields='__all__'   
        
class SencesSerializers(serializers.ModelSerializer):
    class Meta:
        model=BmsScenes
        fields='__all__' 
        depth = 1
        
class BmsTriggerSerializers(serializers.ModelSerializer):
    class Meta:
        model = BmsTriggers
        # fields = ['user_data','card_id','user_card_name','devices_details','card_slug','status','created_at']
        # fields='__all__'
        fields = ['id','trigger_name','action_type','status','trigger_data']
        depth = 1


# POST        
class BmsTriggerSerializersPost(serializers.ModelSerializer):
    # user_data = serializers.IntegerField(source='user_id')
    class Meta:
        model = BmsTriggers
        fields = '__all__'
        # depth = 1 
        
        
        

class BmsDeviceInformationSerializerPo(serializers.ModelSerializer):
    class Meta:
        model = BmsDeviceInformation
        fields = '__all__'


# post area
class BmsAreaMasterSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsAreaMaster
        fields = '__all__'
        # depth=10


# GET Sub_area

class BmsDeviceInformationSerializerPo(serializers.ModelSerializer):
    class Meta:
        model = BmsDeviceInformation
        # fields = '__all__'
        fields=['id','device_name','device_type','is_used','status','is_deleted','create_at','updated_at','device_informations']

class BmsSubAreaMasterSerializer(serializers.ModelSerializer):
    devices_details=BmsDeviceInformationSerializerPo(many=True)
    area_data=BmsAreaMasterSerializer(source='area', read_only=True)
    class Meta:
        model = BmsSubAreaMaster
        # fields = '__all__'
        fields = ['id','sub_area_name','on_image_path','off_image_path','width','height','seating_capacity','status','area_data','devices_details']
        depth = 10


# post Sub_area
class BmsSubAreaMasterSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsSubAreaMaster
        fields = '__all__'


# GET Locker
class BmsSubAreaMasterSerializerss(serializers.ModelSerializer):
    # devices_details=BmsDeviceInformationSerializerPo(many=True)
    class Meta:
        model = BmsSubAreaMaster
        # fields = '__all__'
        fields = ['id','sub_area_name','on_image_path','off_image_path','width','height','seating_capacity','status','is_deleted']
        # depth = 10
class BmsLockerSerializer(serializers.ModelSerializer):
    sub_area_details= BmsSubAreaMasterSerializerss(source='sub_area',read_only=True)
    class Meta:
        model = BmsLocker
        # fields = '__all__'
        fields=['id','category','locker_name','status','sub_area_details']
        # depth = 10


# post Locker
class BmsLockerSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsLocker
        fields ='__all__'


# GET
class BmsHardwareTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsHardwareTypeMaster
        fields = '__all__'
        depth = 10


# GET Device Type
class BmsDeviceTypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsDeviceTypeMaster
        fields = '__all__'
        depth = 10


# Post Device type
class BmsDeviceTypeMasterSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsDeviceTypeMaster
        fields = '__all__'


# GET Device informations
class BmsDeviceInformationSerializer(serializers.ModelSerializer):
    hardware_details_id = serializers.SerializerMethodField()
    hardware_type_name = serializers.SerializerMethodField()
    hardware_name = serializers.SerializerMethodField()
    
    

    class Meta:
        model = BmsDeviceInformation
        fields = ['id','device_name','device_type','hardware_details_id','hardware_type_name','hardware_name','is_used','device_informations','status','is_deleted','create_at']
        # depth = 10
        
        
    def get_hardware_details_id(self, obj):
        if obj.hardware_details:
            return obj.hardware_details.id
        return None
    
    
    def get_hardware_type_name(self, obj):
        if obj.hardware_details:
            return obj.hardware_details.hardware_type.hardware_type_name
        return None
    
    
    def get_hardware_name(self, obj):
        if obj.hardware_details:
            return obj.hardware_details.hardware_name
        return None
        
# post Device Informations


class BmsDeviceInformationSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsDeviceInformation
        fields = '__all__'


# GET
class BmsDeviceStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsDeviceStatusHistory
        fields = '__all__'
        depth = 10

# GET

class BmsUserAreaCardsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsUserAreaCardsList
        # fields = ['user_data','card_id','user_card_name','device_details','card_slug','status','created_at']
        fields='__all__'
        depth = 1


# POST        
class BmsUserAreaCardsListSerializerPost(serializers.ModelSerializer):
    # user_data = serializers.IntegerField(source='user_id')
    class Meta:
        model = BmsUserAreaCardsList
        fields = '__all__'
        # depth = 1
        
        
# Put 

class BmsUserAreaCardsListSerializerPut(serializers.ModelSerializer):
    # user_data = serializers.IntegerField(source='user_id')
    class Meta:
        model = BmsUserAreaCardsList
        fields = ['user','card_id','column_no','user_card_name','card_title','card_slug','status','device_details']
        # depth = 1




## 4/5/2023 


# class BmsSubAreaMasterSerializers(serializers.ModelSerializer):
#     # floor_id = BmsFloorMasterSerializer(many=True, read_only=True)
#     # area_id = BmsAreaMasterSerializer(many=True, read_only=True)
#     class Meta:
#         model = BmsSubAreaMaster
#         fields = ['id','sub_area_name','width','height','status','on_image_path','off_image_path','devices_details']
#         depth = 10


class BmsDeviceInformationSerializerPo(serializers.ModelSerializer):
    class Meta:
        model = BmsDeviceInformation
        # fields = '__all__'
        fields=['device_name','device_type','is_used','status','is_deleted','create_at','updated_at','device_informations']

class BmsSubAreaMasterSerializers(serializers.ModelSerializer):
    devices_details=BmsDeviceInformationSerializerPo(many=True)
    class Meta:
        model = BmsSubAreaMaster
        # fields = '__all__'
        fields = ['sub_area_name','on_image_path','off_image_path','width','height','seating_capacity','status','is_deleted','devices_details']
        depth = 10




class BmsAreaMasterSerializers(serializers.ModelSerializer):
    sub_areas_data=BmsSubAreaMasterSerializers(many=True)
    class Meta:
        model = BmsAreaMaster
        fields = ['id','area_name','status','created_at','updated_at','sub_areas_data']
        # fields='__all__'
        # depth = 10

    def create(self, validated_data):
        user_hobby = validated_data.pop('sub_areas_data')
        profile_instance = BmsAreaMaster.objects.create(**validated_data)
        for hobby in user_hobby:
            BmsSubAreaMaster.objects.create(user=profile_instance,**hobby)
        return profile_instance
         
class BmsFloorMasterSerializers(serializers.ModelSerializer):
    areas_data=BmsAreaMasterSerializers(many=True)
    class Meta:

        model = BmsFloorMaster
        # fields ='__all__'
        fields=['id','floor_name','status','created_at','updated_at','areas_data']
        # depth = 10
        
    def create(self, validated_data):
        user_hobby = validated_data.pop('areas_data')
        profile_instance = BmsFloorMaster.objects.create(**validated_data)
        for hobby in user_hobby:
            BmsAreaMaster.objects.create(user=profile_instance,**hobby)
        return profile_instance
        
     
class ProfileSerializer(serializers.ModelSerializer):
    floor_data = BmsFloorMasterSerializers(many=True)

    class Meta:
        model = BmsBuildingMaster
        # fields = '__all__'
        fields=['id','tower_name','status','created_at','updated_at','is_deleted','floor_data']
        # depth = 10

    def create(self, validated_data):
        user_hobby = validated_data.pop('floor_data')
        profile_instance = BmsBuildingMaster.objects.create(**validated_data)
        for hobby in user_hobby:
            BmsFloorMaster.objects.create(user=profile_instance,**hobby)
        return profile_instance
    




## scence serializer




class SencesSerializers(serializers.ModelSerializer):
    class Meta:
        model=BmsSceneAppliancesDetails
        # fields='__all__' 
        fields=['device_type_slug','component_id','component_name','operation_type','operation_value']
        # depth = 1

        
class ProfileSerializerssss(serializers.ModelSerializer):
    scene_appliance_details = SencesSerializers(many=True)

    class Meta:
        model = BmsScenes
        # fields = '__all__'
        fields=['id','scene_name','status','created_at','updated_at','scene_appliance_details']
        depth = 10

    def create(self, validated_data):
        scene_appliance_details = validated_data.pop('scene_appliance_details')
        scene_instance = BmsScenes.objects.create(**validated_data)
        for detail in scene_appliance_details:
            BmsSceneAppliancesDetails.objects.create(scene=scene_instance, **detail)
        return scene_instance
    
    
    
    
    
## user History


class UserHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model=BmsHistory
        fields='__all__' 
        # fields=['device_type_slug','component_id','operation_type','operation_value']
        # depth = 1
 
 
### 08/06/2024       
        
class BmsHardwareTypeMasterSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=BmsHardwareTypeMaster
        fields='__all__'
        
        
class BmsHardWareDetailsSerializers(serializers.ModelSerializer):
    hardware_type_name = serializers.SerializerMethodField()
    hardware_type_id= serializers.SerializerMethodField()
    

    class Meta:
        model = BmsHardWareDetails
        fields = ['id', 'hardware_type_name','hardware_type_id', 'hardware_name', 'hardware_details', 'status', 'is_deleted', 'updated_at']

    def get_hardware_type_name(self, obj):
        if obj.hardware_type:
            return obj.hardware_type.hardware_type_name
        return None
    
    def get_hardware_type_id(self, obj):
        if obj.hardware_type:
            return obj.hardware_type.id
        return None

        
        
class BmsHardWareDetailsSerializersPost(serializers.ModelSerializer):
    # hardware_type_data = BmsHardwareTypeMasterSerializers(source='hardware_type', read_only=True)
     # hardware_type= serializers.PrimaryKeyRelatedField(queryset=BmsHardwareTypeMaster.objects.all())
    
    class Meta:
        model=BmsHardWareDetails
        # fields='__all__'
        fields=['id','hardware_name','hardware_details','status','updated_at','hardware_type']
        
        
        

class BmsHardWareDetailsSerializersPut(serializers.ModelSerializer):
    # hardware_type_data = BmsHardwareTypeMasterSerializers(source='hardware_type', read_only=True)
     # hardware_type= serializers.PrimaryKeyRelatedField(queryset=BmsHardwareTypeMaster.objects.all())
    
    class Meta:
        model=BmsHardWareDetails
        fields='__all__'
        # fields=['id','hardware_name','hardware_details','status','updated_at','hardware_type']
