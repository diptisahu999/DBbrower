from rest_framework import serializers
from Authenticate.models import BmsModuleMaster, BmsRole, BmsUserType, BmsUser, BmsUsersDetail, BmsRolesDevicesInformation
from Device.models import BmsDepartmentMaster, BmsLocker


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsModuleMaster
        fields = ["id",
                  "module_name",
                  "module_slug",
                  "status",]


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsRole
        fields = ['id', 'role_name', 'modules_data']


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsUserType
        fields = ['id']


class DepertmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsDepartmentMaster
        fields = ['department_name']


class lockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsLocker
        fields = ['locker_name']


class BmsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsUsersDetail
        fields ='__all__'
        depth = 10


class BmsUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        # role_id=RoleSerializer(many=True,read_only=True)
        # user_details=BmsUserSerializer(write_only=True)
        # department_id=DepertmentSerializer(many=True,read_only=True)
        # locker_id=lockerSerializer(many=True,read_only=True)
        model = BmsUser
        fields = ('id','user_email','user_password','domain_type')
        depth = 10


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = BmsUser
        fields = '__all__'
        depth = 10


# user registation

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BmsUsersDetail
#         fields = '__all__'


# user Views
class Manage_user_view(serializers.ModelSerializer):
    class Meta:
        model = '__all__'


class RolesDeviceInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmsRolesDevicesInformation
        # fields = '__all__'
        fields = ['id', 'role_id', 'subarea_id',
                  'device_information_id', 'created_date']

        depth = 10


class RolesDeviceInformationSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = BmsRolesDevicesInformation
        # fields = '__all__'
        fields = ['id', 'role_id', 'device_information_id']
        # depth=10
