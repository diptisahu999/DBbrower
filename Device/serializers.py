from rest_framework import serializers
from Device.models import *

# GET Building


class BmsBuildingMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsBuildingMaster
        fields = '__all__'
        depth=10

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
        
        
        


# post area
class BmsAreaMasterSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsAreaMaster
        fields = '__all__'
        depth=10


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
        fields = '__all__'
        depth = 10






## 4/5/2023 


class BmsSubAreaMasterSerializers(serializers.ModelSerializer):
    # floor_id = BmsFloorMasterSerializer(many=True, read_only=True)
    # area_id = BmsAreaMasterSerializer(many=True, read_only=True)
    class Meta:
        model = BmsSubAreaMaster
        fields = '__all__'
        depth = 10




class BmsAreaMasterSerializers(serializers.ModelSerializer):
    sub_areas_data=BmsSubAreaMasterSerializers(many=True)
    class Meta:
        model = BmsAreaMaster
        fields = '__all__'
        depth = 10

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
        fields ='__all__'
        depth = 10
        
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
        fields = '__all__'
        depth = 10

    def create(self, validated_data):
        user_hobby = validated_data.pop('floor_data')
        profile_instance = BmsBuildingMaster.objects.create(**validated_data)
        for hobby in user_hobby:
            BmsFloorMaster.objects.create(user=profile_instance,**hobby)
        return profile_instance