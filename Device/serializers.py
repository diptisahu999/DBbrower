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


class BmsFloorMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsFloorMaster
        fields ='__all__'
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
    class Meta:
        model = BmsAreaMaster
        fields = '__all__'
        depth = 10




    
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
        fields='__all__'
        depth = 2


# POST        
class BmsTriggerSerializersPost(serializers.ModelSerializer):
    # user_data = serializers.IntegerField(source='user_id')
    class Meta:
        model = BmsTriggers
        fields = '__all__'
        # depth = 1 
        
        
        


# post area
class BmsAreaMasterSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsAreaMaster
        fields = '__all__'
        # depth=10


# GET Sub_area
class BmsSubAreaMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsSubAreaMaster
        fields = '__all__'
        depth = 10


# post Sub_area
class BmsSubAreaMasterSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsSubAreaMaster
        fields = '__all__'


# GET Locker
class BmsLockerSerializer(serializers.ModelSerializer):
    # sub_area_id = BmsSubAreaMasterSerializer(many=True, read_only=True)
    class Meta:
        model = BmsLocker
        fields = '__all__'
        depth = 10


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

    class Meta:
        model = BmsDeviceInformation
        fields = '__all__'
        depth = 10
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
        fields = ['user_data','card_id','column_no','user_card_name','card_title','card_slug','status','device_details']
        # depth = 1




## 4/5/2023 




class BmsSubAreaMasterSerializers(serializers.ModelSerializer):
    # floor_id = BmsFloorMasterSerializer(many=True, read_only=True)
    # area_id = BmsAreaMasterSerializer(many=True, read_only=True)
    class Meta:
        model = BmsSubAreaMaster
        fields = ['id','sub_area_name','width','height','status','on_image_path','off_image_path','devices_details']
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
        fields=['id','tower_name','status','created_at','updated_at','floor_data']
        # depth = 10

    def create(self, validated_data):
        user_hobby = validated_data.pop('floor_data')
        profile_instance = BmsBuildingMaster.objects.create(**validated_data)
        for hobby in user_hobby:
            BmsFloorMaster.objects.create(user=profile_instance,**hobby)
        return profile_instance