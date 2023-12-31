from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response 
from Authenticate.models import *
from Authenticate.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from Device.serializers import *
from Device.models import BmsSubAreaMaster
import numpy as np



import time
import requests
import schedule


# login api


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)
    
    

class LoginView(APIView):
    def post(self, request, format=None):
        login_serializer=LoginSerializer(data=request.data)
        
        if login_serializer.is_valid():
            user_email=login_serializer.data.get('user_email')
            user_password=login_serializer.data.get('user_password')
            try:
                user=BmsUser.objects.get(user_email=user_email, user_password=user_password)
                token=get_tokens_for_user(user)
            except BmsUser.DoesNotExist:
                return Response({"status_code": 401,'error':{'Email or password is not valid'}},status=status.HTTP_400_BAD_REQUEST)
            userDetails = BmsUser.objects.get(user_email=user.user_email) # retrieve user by user_id
            tutorials_serializer = BmsUserDetailsSerializers(userDetails)
            
            return Response({"data":"true","status_code": 200,"access_token":str(token),"message": "Login Successfully","response":tutorials_serializer.data},status=status.HTTP_200_OK)
        return Response({"status_code":401,"responce":login_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
 
    
    

# class LoginView(APIView):
#     def post(self, request, format=None):
#         login_serializer=BmsUserDetailsSerializer(data=request.data)
        
#         if login_serializer.is_valid():
#             user_email=login_serializer.data.get('user_email')
#             user_password=login_serializer.data.get('user_password')
#             try:
#                 user=BmsUser.objects.get(user_email=user_email, user_password=user_password)
#             except BmsUser.DoesNotExist:
#                 return Response({"status_code": 401,'error':{'User not Found':'Email or password is not valid'}},status=status.HTTP_201_CREATED)
#             userDetails = BmsUser.objects.get(user_email=user.user_email) 
#             tutorials_serializer = BmsUserDetailsSerializer(userDetails, many=False)
#             return Response({"data":"true","status_code": 200,"message": "Login Successfully", "response":tutorials_serializer.data})
#         return Response({"status_code":401,"responce":login_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
 
      
 # user list crud    


@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        bms_users = BmsUser.objects.filter(is_deleted="No")
        bms_users_serializer = BmsUserDetailsSerializer(bms_users, many=True)
        return Response({"data": True, "status_code": 200, "message": "User Lists", "response": bms_users_serializer.data},
                        status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # input("111")   
        print(request.data)
        data = request.data
        # data["user_type_data"] = data.pop("user_type_id")
        # data["role_data"] = data.pop("role_id")
        # print(request.data)
        # a= input("hello world")


        user_serializer = BmsUserDetailsSerializerPost(data=request.data)
        print(request.data)
        # input("111")  
        if user_serializer.is_valid():
            user_email = user_serializer.validated_data.get('user_email')
            # Check if the user_email already exists
            if BmsUser.objects.filter(user_email=user_email).exists():
                return Response({"status_code": 400, "message": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            
        user = user_serializer.save()
        try:
            user_detail_data = {
                    'user_data': user.id,  # Set the foreign key to the newly created user
                    'first_name': request.data['user_details'].get('first_name'),
                    'last_name': request.data['user_details'].get('last_name'),
                    'phone_no': request.data['user_details'].get('phone_no'),
                    'dob': request.data['user_details'].get('dob'),
                    'wallet_balance': request.data['user_details'].get('wallet_balance'),
                    'has_vehicle': request.data['user_details'].get('has_vehicle'),
                    'locker_data': request.data['user_details'].get('locker_data'),
                    "address":request.data['user_details'].get('address'),
                    "id_proof":request.data['user_details'].get('id_proof'),
                    "visiting_card":request.data['user_details'].get('visiting_card'),
                    "is_deleted":request.data['user_details'].get('is_deleted'),
                    # Add other fields as per your model
                }
        except:
            user_detail_data = {
                'user_data': user.id,  # Set the foreign key to the newly created user
                # Add other fields for BmsUsersDetail model
                'first_name': None,
                'last_name': None ,
                # Add other fields as per your model  
            }


        user_detail_data = {k: v for k, v in user_detail_data.items() if v is not None}

        try:
            user_detail_serializer = BmsUserSerializerUser(data=user_detail_data)
            user_detail_serializer.is_valid(raise_exception=True)
            user_detail_serializer.save()
            print(user_detail_serializer.data)
        except serializers.ValidationError as e:
            return Response({"status_code": 400, "message": "Invalid data", "errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

        # token = get_tokens_for_user(user)
        
        return Response({"data": "true", "status_code": 200,"message": "User Added Successfully", "response": user_serializer.data}, status=status.HTTP_201_CREATED)
    
        return Response({"status_code": 400, "response": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'DELETE':
    #     count = BmsUser.objects.all().delete()
    #     return Response({'message': '{} User was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    


# example
# def your_view(request):
#     if request.method == 'DELETE':
#         instance = # Get your instance to delete
#         confirmation = request.data.get('confirmation', None)
#         if confirmation == 'yes':
#             # Perform the deletion
#             instance.delete()
#             return Response({'message': 'Record deleted.'}, status=200)
#         else:
#             return Response({'message': 'Deletion not confirmed.'}, status=400)

 
 
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def user(request, pk):
    try: 
        bms_users = BmsUser.objects.get(pk=pk) 
    except BmsUser.DoesNotExist: 
        return Response({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        bms_uses_serializer = BmsUserDetailsSerializer(bms_users) 
        # return Response(bms_uses_serializer.data) 
        return Response({"data":"true","status_code": 200, "message": "User Get Successfully", "response":bms_uses_serializer.data},status=status.HTTP_200_OK)
        
 
    elif request.method == 'PUT':  
        data = request.data
        bms_uses_serializer = BmsUserDetailsSerializerPost(bms_users, data=data)
        try:
            const_data=request.data
            user_detail= const_data['user_details']
            Bms_user_detail = BmsUsersDetail.objects.get(pk=user_detail['id']) 
            
            bms_user_Details_serializer = BmsUserSerializerss(Bms_user_detail,data=user_detail)
            if bms_user_Details_serializer.is_valid() & bms_uses_serializer.is_valid():
                bms_user_Details_serializer.save()
                bms_uses_serializer.save()
                # return Response(bms_uses_serializer.data) 
                return Response({"data":"true","status_code": 200, "message": "User Updated Successfully"},status=status.HTTP_201_CREATED)
        except:
            bms_uses_serializer.is_valid()
            bms_uses_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "User Updated Successfully"},status=status.HTTP_201_CREATED)
            
        return Response({"status_code":401,"responce":[bms_uses_serializer.errors ,bms_user_Details_serializer.errors]},status=status.HTTP_400_BAD_REQUEST)  
 
 
    # elif request.method == 'DELETE': 
    #     bms_users.delete() 
    #     return Response({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
    elif request.method == 'DELETE':
        confirmation = request.data.get('confirmation', None)
        if confirmation == 'yes':
            bms_users.delete()
            return Response({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'Deletion not confirmed.'}, status=status.HTTP_400_BAD_REQUEST)
    

# role crud

    
@api_view(['GET', 'POST', 'DELETE'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def role_list(request): 
    if request.method == 'GET':
        bms_role = BmsRole.objects.all() 
        bms_role_serializer = RoleSerializer(bms_role, many=True)
        return Response({"data":"true","status_code": 200, "message": "Role Lists", "response":bms_role_serializer.data},status=status.HTTP_200_OK)
        
    # elif request.method == 'POST':
    #     role_serializer = RoleSerializer(data=request.data)
    #     if role_serializer.is_valid():
    #         user=role_serializer.save()
    #         # token=get_tokens_for_user(user)
    #         return Response({"data":"true","status_code": 200, "message": "Role Added Successfully!!","response":role_serializer.data})
    #         # return Response({"data":"true","status_code": 200, "message": "User role created Successfully!!",'token':token, "response":tutorial_serializer.data})
    #     return Response({"status_code":401,"responce":role_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    
    
    elif request.method == 'POST':
        role_serializer = RoleSerializerPost(data=request.data)
        if role_serializer.is_valid():
            role_name = role_serializer.validated_data.get('role_name')
            
            # Check if a role with the same name already exists
            if BmsRole.objects.filter(role_name=role_name).exists():
                return Response({
                    "status_code": 400,
                    "message": "Role with the same name already exists."
                }, status=status.HTTP_400_BAD_REQUEST)
            
            role_serializer.save()
            return Response({
                "data": "true",
                "status_code": 200,
                "message": "Role Added Successfully!!",
                "response": role_serializer.data
            },status=status.HTTP_201_CREATED)
        
        return Response({
            "status_code": 400,
            "response": role_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    # elif request.method == 'POST':
    #     role_serializer = RoleSerializerPost(data=request.data)
    #     if role_serializer.is_valid():
    #         role_name = role_serializer.validated_data.get('role_name')

    #         # Check if a role with the same name already exists
    #         if BmsRole.objects.filter(role_name=role_name).exists():
    #             return Response({
    #                 "status_code": 400,
    #                 "message": "Role with the same name already exists."
    #             }, status=status.HTTP_400_BAD_REQUEST)

    #         assigned_device_data = role_serializer.validated_data.get('device_data')

    #         # Check if the assigned device_data is already assigned to another role
    #         if BmsRole.objects.filter(device_data__in=assigned_device_data).exclude(role_name=role_name).exists():
    #             return Response({
    #                 "status_code": 400,
    #                 "message": "Device data is already assigned to another role."
    #             }, status=status.HTTP_400_BAD_REQUEST)

    #         role_serializer.save()
    #         return Response({
    #             "data": "true",
    #             "status_code": 200,
    #             "message": "Role Added Successfully!!",
    #             "response": role_serializer.data
    #         },status=status.HTTP_201_CREATED)
        
    #     return Response({
    #         "status_code": 400,
    #         "response": role_serializer.errors
    #     }, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'POST':
    #     role_serializer = RoleSerializer(data=request.data)
    #     if role_serializer.is_valid():
    #         # Perform additional validations here
    #         # For example, you can access specific fields and perform custom checks
    #         if role_serializer.validated_data['field_name'] != expected_value :
    #             return Response({"status_code": 400, "message": "Invalid field value."})
            
    #         user = role_serializer.save()
    #         return Response({
    #             "data": "true",
    #             "status_code": 200,
    #             "message": "Role Added Successfully!!",
    #             "response": role_serializer.data
    #         })
    #     return Response({
    #     "status_code": 400,
    #     "response": role_serializer.errors
    # }, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'DELETE':
    #     count = BmsRole.objects.all().delete()
    #     return Response({'message': '{} Role deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def role_detail(request, pk):
    try: 
        bms_role = BmsRole.objects.get(pk=pk)
    except BmsRole.DoesNotExist: 
        return Response({'message': 'The User Role does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
 
    if request.method == 'GET': 
        bms_role_serializer = RoleSerializer(bms_role) 
        return Response({"data":"true","status_code": 200, "message": "Role Get Successfully", "response":bms_role_serializer.data},status=status.HTTP_200_OK) 
 
#     elif request.method == 'PUT': 
#         data=request.data      
#         bms_role_serializer = RoleSerializerPut(bms_role, data=data )
#         if bms_role_serializer.is_valid(): 
#             bms_role_serializer.save() 
#             # return Response({"data":"true","status_code": 200, "message": "Role Updated Sucessfuly!!","response":bms_role_serializer.data}) 
        
#         if 'device_data'  in data:
#             bms_role_serializer = RoleSerializer(bms_role)
#             data = bms_role_serializer.data['device_data']
#             return Response({"data":"true","status_code": 200, "message": "Role Device Information Added Sucessfuly!!","response":data},status=status.HTTP_201_CREATED) 
        
#         elif 'modules_permission'  in data:
#             bms_role_serializer = RoleSerializer(bms_role)
#             data = bms_role_serializer.data['modules_permission']
#             return Response({"data":"true","status_code": 200, "message": "Modules Added Succesfully!!","response":data},status=status.HTTP_201_CREATED) 
        
#         return Response({"status_code":401,"responce":bms_role_serializer.errors},status=status.HTTP_400_BAD_REQUEST)  


    elif request.method == 'PUT': 
        data = request.data   
        print(data)   
        bms_role_serializer = RoleSerializerPut(bms_role, data=data)
        if bms_role_serializer.is_valid(): 
            # Check if the assigned device_data is already assigned to another role
            # if 'device_data' in data and BmsRole.objects.filter(device_data__in=data['device_data']).exclude(role_name=bms_role.role_name).exists():
            #     return Response({
            #         "status_code": 400,
            #         "message": "Device data is already assigned to another role."
            #     }, status=status.HTTP_400_BAD_REQUEST)

            bms_role_serializer.save()
            return Response({
                "data": "true",
                "status_code": 200,
                "message": "Role Updated Successfully!!",
                "response": bms_role_serializer.data
            })

        return Response({"status_code": 401, "response": bms_role_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE': 
#         bms_role.delete() 
#         return Response({'message': 'Role was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def role_detail(request, pk):
#     try: 
#         bms_role = BmsRole.objects.get(pk=pk)
#     except BmsRole.DoesNotExist: 
#         return Response({'message': 'The User Role does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
#     if request.method == 'GET': 
#         bms_role_serializer = RoleSerializer(bms_role) 
#         return Response({"data":"true","status_code": 200, "message": "Role Get Successfully", "response":bms_role_serializer.data},status=status.HTTP_200_OK) 
    
#     elif request.method == 'PUT': 
#         data = request.data      
#         bms_role_serializer = RoleSerializerPut(bms_role, data=data)
#         if bms_role_serializer.is_valid(): 
#             # Check if the assigned device_data is already assigned to another role
#             if 'device_data' in data and BmsRole.objects.filter(device_data__in=data['device_data']).exclude(role_name=bms_role.role_name).exists():
#                 return Response({
#                     "status_code": 400,
#                     "message": "Device data is already assigned to another role."
#                 }, status=status.HTTP_400_BAD_REQUEST)

#             bms_role_serializer.save()
#             return Response({
#                 "data": "true",
#                 "status_code": 200,
#                 "message": "Role Updated Successfully!!",
#                 "response": bms_role_serializer.data
#             })

#         return Response({"status_code": 401, "response": bms_role_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  

#     elif request.method == 'DELETE': 
#         bms_role.delete() 
#         return Response({'message': 'Role was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
    
    
# Bms_Users_Details table crud

@api_view(['GET', 'POST', 'DELETE'])
# @permission_classes([IsAuthenticated])
def user_details_list(request):
    if request.method == 'GET':
        user_details = BmsUsersDetail.objects.filter(is_deleted="No")
        user_details_serializer = BmsUserSerializer(user_details, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "User Profile Details Lists", "response":user_details_serializer.data},status=status.HTTP_200_OK)
 
    elif request.method == 'POST':
        details_serializer = BmsUserSerializer(data=request.data)
        if details_serializer.is_valid():
            details_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "User Details Added Sucessfuly!!","response":details_serializer.data},status=status.HTTP_201_CREATED) 
        return Response({"status_code":401,"responce":details_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        count = BmsUsersDetail.objects.all().delete()
        return Response({'message': '{} User details was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def user_detail(request, pk):
    try: 
        user_details = BmsUsersDetail.objects.get(pk=pk) 
    except BmsUsersDetail.DoesNotExist: 
        return Response({'message': 'The User details does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # return JsonResponse({'message': 'The User details does not exist'}, status=status.HTTP_404_NOT_FOUND) 
         
 
    if request.method == 'GET': 
        user_details_serializer =BmsUserSerializer(user_details) 
        return Response({"data":"true","status_code": 200, "message": "Get Data Successfully", "response":user_details_serializer.data},status=status.HTTP_200_OK) 
 
    elif request.method == 'PUT': 
        user_details_serializer = BmsUserSerializer(user_details, data=request.data) 
        if user_details_serializer.is_valid(): 
            user_details_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "User details updated Sucessfuly!!","response":user_details_serializer.data},status=status.HTTP_201_CREATED)
        return Response({"status_code":401,"responce":user_details_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
         
 
    elif request.method == 'DELETE': 
        user_details.delete() 
        return Response({'message': 'User details deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
# Bms_Module crud

@api_view(['GET', 'POST', 'DELETE'])
# @permission_classes([IsAuthenticated])
def module_list(request):
    if request.method == 'GET':
        bms_module = BmsModuleMaster.objects.all()        
        bms_module_serializer = ModuleSerializer(bms_module, many=True)
        return Response({"data":"true","status_code": 200, "message": "Module Lists", "response":bms_module_serializer.data},status=status.HTTP_200_OK)
    
 
    elif request.method == 'POST':
        module_serializer = ModuleSerializer(data=request.data)
        if module_serializer.is_valid():
            module_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Module Added Sucessfuly!!","response":module_serializer.data},status=status.HTTP_201_CREATED) 
        return Response({"status_code":401,"responce":module_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        count = BmsModuleMaster.objects.all().delete()
        return Response({'message': '{} Module was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
 
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def module_detail(request, pk):
    try: 
        bms_module = BmsModuleMaster.objects.get(pk=pk) 
    except BmsModuleMaster.DoesNotExist: 
        return Response({'message': 'The Module does not exist'}, status=status.HTTP_404_NOT_FOUND) 
         
 
    if request.method == 'GET': 
        module_serializer = ModuleSerializer(bms_module) 
        return Response({"data":"true","status_code": 200, "message": "Role Get Successfully", "response":module_serializer.data},status=status.HTTP_200_OK)  
 
    elif request.method == 'PUT': 
        module_serializer = ModuleSerializer(bms_module, data=request.data) 
        if module_serializer.is_valid(): 
            module_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Module updated Sucessfuly!!","response":module_serializer.data},status=status.HTTP_201_CREATED) 
        return Response({"status_code":401,"responce":module_serializer.errors},status=status.HTTP_400_BAD_REQUEST)  
         
 
    elif request.method == 'DELETE': 
        bms_module.delete() 
        return Response({'message': 'Module was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
 # role_device_informations_list crud   

@api_view(['GET', 'POST', 'DELETE'])
# @permission_classes([IsAuthenticated])
def role_device_information_list(request):
    if request.method == 'GET':
        bms_module = BmsRolesDevicesInformation.objects.all()        
        bms_module_serializer = RolesDeviceInformationSerializer(bms_module, many=True)
        return Response({"data":"true","status_code": 200, "message": "Role Device Information Lists", "response":bms_module_serializer.data})
    
 
    elif request.method == 'POST':
        module_serializer = RolesDeviceInformationSerializerPost(data=request.data)
        if module_serializer.is_valid():
            module_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Role Device Information Added Sucessfuly!!","response":module_serializer.data},status=status.HTTP_201_CREATED) 
        return Response({"status_code":401,"responce":module_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    
    # elif request.method == 'POST':
       
    #     data = request.data
    #     sub_area_ids = data['subarea_id']
    #     # print(Floor_ids)
    #     for sub_area in sub_area_ids:
    #         area = dict(data)
    #         area.update({'subarea_id': sub_area})
    #         # print(area)    
    #         serializer = RolesDeviceInformationSerializerPost(data=area)
    #         if serializer.is_valid():
    #             serializer.save()
    #         else:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     return Response({'data': 'true', 'status_code': 200, 'message': 'Data added successfully'})  
        
    
    # elif request.method == 'DELETE':
    #     count = BmsRolesDevicesInformation.objects.all().delete()
    #     return Response({'message': '{} Module was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
 
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def role_device_information_details(request, pk):
    try:
        # bms_roles_device_information
        bms_module = BmsRolesDevicesInformation.objects.get(pk=pk) 
    except BmsModuleMaster.DoesNotExist: 
        return Response({'message': 'Role Device Information does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # return JsonResponse({'message': 'Role Device Information does not exist'}, status=status.HTTP_404_NOT_FOUND) 
         
 
    if request.method == 'GET': 
        module_serializer = RolesDeviceInformationSerializer(bms_module) 
        return Response({"data":"true","status_code": 200, "message": "Role Get Successfully", "response":module_serializer.data},status=status.HTTP_200_OK) 
 
    elif request.method == 'PUT': 
        module_serializer = RolesDeviceInformationSerializer(bms_module, data=request.data) 
        if module_serializer.is_valid(): 
            module_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Role Device Information updated Sucessfuly!!","response":module_serializer.data},status=status.HTTP_201_CREATED) 
        return Response({"status_code":401,"responce":module_serializer.errors},status=status.HTTP_400_BAD_REQUEST)  
         
 
    elif request.method == 'DELETE': 
        bms_module.delete() 
        return Response({"message": "Role Device Information  deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)





@api_view(['GET','POST','DELETE'])
def get_tower_list(request):
    if request.method == 'GET': 
        return Response({"data":"true","status_code": 200, "response":"This Method not Allowed "}) 


    elif request.method == 'POST':
        data = request.data
        # print(data)
        devices_data= []
        try: 
             device_type = data['device_type']
        except:
            pass
        
        # aaa= input("test 1")
        # print(device_type)
        # try:
        #     # print(data)
        #     data['user_data'] = data.pop('user_id')

           
        # except:
        #     return Response({"data":"true","status_code": 405, "message": "user_id does not exist"})
        # print(data['user_data'])
        # print(data['user_id'])

        try:
            user_details = BmsUser.objects.get(pk=data['user_id'])
        except BmsUser.DoesNotExist:
            return Response({'message': 'The User details do not exist'}, status=status.HTTP_404_NOT_FOUND)

        user_details_serializer = BmsUserSerializer_DeviceDetails(user_details)
        a = (user_details_serializer.data)
        # aaa = input("test 2")
        print(a)
        # f= BmsSubAreaMasterSerializer()
        # print(f.data)

        user_devices_data = (a["role"]["device_data"])
        user_devices_data_list = []
        # print(user_devices_data_list)
        for i in user_devices_data:
            try:
                if i['device_type'] == device_type:
                    user_devices_data_list.append(i)
            except:
                pass
            user_devices_data_list.append(i)


        # print(user_devices_data_list)
        # print(user_devices_data_list ,"mylistinggg")
        # aaa = input("test 2")

        tower_data=[]

        #30may 2023
        for i in user_devices_data_list:
            # print(i ,"loop 1 started")
            if i['device_type'] == device_type:
                # print(i ,"my device")
                sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=i['id'])
                print(i['id'],i['device_type'], "dasdasdasdasdasdasdas")
                # aaa = input("test 3")


                for sub_area in sub_area_instances:
                    print(sub_area)
                    sub_area_name = sub_area.sub_area_name
                    # print(sub_area_name)
                    # tower_list = sub_area.area_data.floor_data.tower_data.id
                    data=  {
                            "id": sub_area.area_data.floor_data.tower_data.id,
                            "tower_name": sub_area.area_data.floor_data.tower_data.tower_name
                        }
                # device= sub_area.devices_details.filter(id=i['id']).values()    
                    device = []
                    # print(data)
                    if not device:
                        pass
                    else:
                # print(device,"me value hu")
                # device_value = serializers.serialize('json',device)
                        devices_data.append(device)
                    tower_data.append(data)  
                



        # a = list(set(tower_data))
        # subarea =  BmsSubAreaMaster.objects.filter(devices_details__device_type="AC")
        # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=17)
        # for i in user_devices_data_list:
            # print(i)
            # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=i)




        # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__device_type=device_type)
        # for sub_area in sub_area_instances:
        #     sub_area_name = sub_area.sub_area_name
        #     print(sub_area_name)
        #     # tower_list = sub_area.area_data.floor_data.tower_data.id
        #     data=  {
        #                 "tower_id": sub_area.area_data.floor_data.tower_data.id,
        #                 "tower_name": sub_area.area_data.floor_data.tower_data.tower_name
        #             }
            
        #     tower_data.append(data)

        unique_data = list(set(tuple(item.items()) for item in tower_data))
        result = [dict(item) for item in unique_data]
        result.sort(key=lambda x: x['id'])
                    # name = i.tower_name
                    # id = i.id
        # print(set(tower_data))
        # print(tower_data)
                # # print(sub_area_name)
                # tower_data.append(tower_list)
      
        return Response({"data":"true","status_code": 200, "message": "User Access List","response": {"tower_data":result}}, status=status.HTTP_200_OK)
        # for i in subarea:
        #     print(i)
        # 
#         floor_data = (a["user_data"]["user_type_data"]['role_data']['subarea_data'])
# # subarea_data ,area_data ,floor_data['subarea_data'],['area_data']['floor_data']
        
#         tower_data = []
#         for i in floor_data:
#             floor_data = (i['area_data']['floor_data'])
#             # print(floor_data)
#             tower_data.append(floor_data['tower_data'])
            
#                 # tower_name = i['tower_data']
#                 # print(tower_name)
#         unique_values = [dict(t) for t in {tuple(d.items()) for d in tower_data}]
#         print(unique_values)
# # "device_data":devices_data
#         tower_data = {"tower_data":unique_values}


        # return Response({"data":"true","status_code": 200, "message": "User Access List","response": {"tower_data":False}}, status=status.HTTP_200_OK)


@api_view(['GET','POST','DELETE'])
def get_tower_device_data(request):

    if request.method == 'GET': 
        return Response({"data":"true","status_code": 200, "response":"This Method not Allowed"}) 


    elif request.method == 'POST':
        data = request.data
        device_type = data['device_type']
        tower_id =data['tower_id']
        Floor_data=[]
        devices_data= []
        # print(data)
        try:
            print(data ,"line 531")
            user_details = BmsUser.objects.get(pk=data['user_id'])
        except BmsUser.DoesNotExist:
            return Response({'message': 'The User details do not exist'}, status=status.HTTP_404_NOT_FOUND)

        user_details_serializer = BmsUserSerializer_DeviceDetails(user_details)
        a = (user_details_serializer.data)
        # aaa = input("test 2")
        print(a)
        # f= BmsSubAreaMasterSerializer()
        # print(f.data)

        user_devices_data = (a["role"]["device_data"])
        user_devices_data_list = []
        for i in user_devices_data:
            
            if device_type == i['device_type']:
                user_devices_data_list.append(i)
        # print(user_devices_data_list)
        #30may 2023
        for i in user_devices_data_list:
            if i['device_type'] == device_type:
                sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__device_type=device_type,area_data__floor_data__tower_data__id=int(tower_id))
                for sub_area in sub_area_instances:
                    sub_area_name = sub_area.sub_area_name
                    # print(sub_area_name)
                    # tower_list = sub_area.area_data.floor_data.tower_data.id
                    data=  {
                        "id": sub_area.area_data.floor_data.id,
                        "floor_name": sub_area.area_data.floor_data.floor_name
                    }
            
            
                    device= sub_area.devices_details.filter(id=i['id']).values()        
                    
                    if not device:
                        pass
                    else:
                    # print(device,"me value hu")
                    # device_value = serializers.serialize('json',device)
                        devices_data.append(device)
                    Floor_data.append(data)





        
       
        # a = list(set(tower_data))
        # subarea =  BmsSubAreaMaster.objects.filter(devices_details__device_type="AC")
        # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=17)
        # for i in user_devices_data_list:
            # print(i)
            # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=i)



        # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__device_type=device_type)
        # for sub_area in sub_area_instances:
        #     sub_area_name = sub_area.sub_area_name
        #     # print(sub_area_name)
        #     # tower_list = sub_area.area_data.floor_data.tower_data.id
            # data=  {
            #             "floor_id": sub_area.area_data.floor_data.id,
            #             "floor_name": sub_area.area_data.floor_data.floor_name
            #         }
            
            # Floor_data.append(data)





        print(Floor_data)
        unique_data = list(set(tuple(item.items()) for item in Floor_data))
        result = [dict(item) for item in unique_data]
        result.sort(key=lambda x: x['id'])

        # unique_data = list(set(tuple(item.items()) for item in devices_data))
        # devices_data = [dict(item) for item in unique_data]
        # devices_data.sort(key=lambda x: x['id'])
        device_data_list = [item[0] for item in devices_data]
        unique_device_data = list({item['id']: item for item in device_data_list}.values())
        sorted_device_data = sorted(unique_device_data, key=lambda x: x['id'])

# "device_data":devices_data
        return Response({"data":"true","status_code": 200, "message": "User Floor and Devices Access list ","response":{"floor_data":result,"device_data":sorted_device_data}}, status=status.HTTP_200_OK)



@api_view(['GET','POST','DELETE'])
def get_floor_device_data(request):
    if request.method == 'GET': 
        return Response({"data":"true","status_code": 200, "response":"This Method not Allowed "}) 


    elif request.method == 'POST':
        data = request.data
        print(data)
        device_type = data['device_type']
        floor_id= data['floor_id']
        print(floor_id)
        # floor_id= 1
        
        area_data=[]
        devices_data= []
        # print(data)
        try:
            print(data ,"line 531")
            user_details = BmsUser.objects.get(pk=data['user_id'])
        except BmsUser.DoesNotExist:
            return Response({'message': 'The User details do not exist'}, status=status.HTTP_404_NOT_FOUND)

        user_details_serializer = BmsUserSerializer_DeviceDetails(user_details)
        a = (user_details_serializer.data)
        # aaa = input("test 2")
        print(a)
        # f= BmsSubAreaMasterSerializer()
        # print(f.data)

        user_devices_data = (a["role_id"]["device_data"])
     
        # f= BmsSubAreaMasterSerializer()
        # print(f.data)
        user_devices_data_list = []
        for i in user_devices_data:
            
            if device_type == i['device_type']:
                user_devices_data_list.append(i)
        # print(user_devices_data_list)
        
       #30may 2023
        for i in user_devices_data_list:
            if i['device_type'] == device_type:
                sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__device_type=device_type,area_data__floor_data__id=int(floor_id))
                for sub_area in sub_area_instances:
                    sub_area_name = sub_area.sub_area_name
                    # print(sub_area_name)
                    # tower_list = sub_area.area_data.floor_data.tower_data.id
                    data=  {
                        "id": sub_area.area_data.id,
                        "area_name": sub_area.area_data.area_name
                    }
                    device= sub_area.devices_details.filter(id=i['id']).values()        
                    
                    if not device:
                        pass
                    else:
                    # print(device,"me value hu")
                    # device_value = serializers.serialize('json',device)
                        devices_data.append(device)
                    area_data.append(data)


        # a = list(set(tower_data))
        # subarea =  BmsSubAreaMaster.objects.filter(devices_details__device_type="AC")
        # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=17)
        # for i in user_devices_data_list:
            # print(i)
            # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=i)




        # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__device_type=device_type)
        # for sub_area in sub_area_instances:
        #     sub_area_name = sub_area.sub_area_name
        #     # print(sub_area_name)
        #     # tower_list = sub_area.area_data.floor_data.tower_data.id
            # data=  {
            #             "area_id": sub_area.area_data.id,
            #             "area_name": sub_area.area_data.area_name
            #         }
        #     area_data.append(data)

        unique_data = list(set(tuple(item.items()) for item in area_data))
        result = [dict(item) for item in unique_data]
        result.sort(key=lambda x: x['id'])

        print(devices_data)
        device_data_list = [item[0] for item in devices_data]
        unique_device_data = list({item['id']: item for item in device_data_list}.values())
        sorted_device_data = sorted(unique_device_data, key=lambda x: x['id'])


        # unique_data = list(set(tuple(item.items()) for item in devices_data))
        # devices_data = [dict(item) for item in unique_data]

        # devices_data.sort(key=lambda x: x['id'])

# "device_data":devices_data
        print(result)
        return Response({"data":"true","status_code": 200, "message": "User Areas and Devices Access list ","response":{"areas_data":result,"device_data":sorted_device_data}}, status=status.HTTP_200_OK)



@api_view(['GET','POST'])
def get_area_device_data(request):
    if request.method == 'GET': 
        return Response({"data":"true","status_code": 200, "response":"This Method not Allowed "}) 


    elif request.method == 'POST':
        data = request.data
        print(data)
        device_type = data['device_type']
        area_id= data['area_id']
        subarea_data=[]
        devices_data= []
        print(data)
        try:
            data['user_data'] = data.pop('user_id')
        except:
            return Response({"data":"true","status_code": 405, "message": "user_id does not exist"})
        # print(data['user_data'])

        try:
            user_details = BmsUser.objects.get(pk=data['user_data'])
        except BmsUser.DoesNotExist:
            return Response({'message': 'The User details do not exist'}, status=status.HTTP_404_NOT_FOUND)

        user_details_serializer = BmsUserSerializer_DeviceDetails(user_details)
        a = (user_details_serializer.data)
     
        # f= BmsSubAreaMasterSerializer()
        # print(f.data)

        user_devices_data = (a["role_id"]["device_data"])
        user_devices_data_list = []
        for i in user_devices_data:
            
            if device_type == i['device_type']:
                user_devices_data_list.append(i)
        # print(user_devices_data_list)
        
        for i in user_devices_data_list:
            if i['device_type'] == device_type:
                sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__device_type=device_type,area_data__id=int(area_id))
                for sub_area in sub_area_instances:
                    sub_area_name = sub_area.sub_area_name
                    # print(sub_area_name)
                    # tower_list = sub_area.area_data.floor_data.tower_data.id
                    data=  {
                                "id": sub_area.id,
                                "sub_area_name": sub_area.sub_area_name
                            }
                    device= sub_area.devices_details.filter(id=i['id']).values()        
                   
                    if not device:
                        pass
                    else:
                    # print(device,"me value hu")
                    # device_value = serializers.serialize('json',device)
                        devices_data.append(device)
                    subarea_data.append(data)






        # a = list(set(tower_data))
        # subarea =  BmsSubAreaMaster.objects.filter(devices_details__device_type="AC")
        # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=17)
        # for i in user_devices_data_list:
            # print(i)
            # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=i)
        # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__device_type=device_type)
        # for sub_area in sub_area_instances:
        #     sub_area_name = sub_area.sub_area_name
        #     # print(sub_area_name)
        #     # tower_list = sub_area.area_data.floor_data.tower_data.id
        #     data=  {
        #                 "sub_area_id": sub_area.id,
        #                 "sub_area_name": sub_area.sub_area_name
        #             }
        #     subarea_data.append(data)
          
        unique_data = list(set(tuple(item.items()) for item in subarea_data))
        result = [dict(item) for item in unique_data]
        result.sort(key=lambda x: x['id'])
        print(result)
        device_data_list = [item[0] for item in devices_data]
        unique_device_data = list({item['id']: item for item in device_data_list}.values())
        sorted_device_data = sorted(unique_device_data, key=lambda x: x['id'])

        return Response({"data":"true","status_code": 200, "message": "User Areas and Devices Access list ","response":{"sub_area_data":result,"device_data":sorted_device_data}}, status=status.HTTP_200_OK)
    
    
  
    
   #{ "user_id":2, "user_role" : "manager", "card_type" : "ac","area_id":1} 
   
   
@api_view(['GET','POST'])
def get_device_data(request):
    if request.method == 'GET': 
        return Response({"data":"true","status_code": 200, "response":"This Method not Allowed "}) 


    elif request.method == 'POST':
        data = request.data
        device_type = data['device_type']
        user_role = data['user_role']
        sub_area_id= data['sub_area_id']
        subarea_data=[]
        devices_data= []
        # print(data)
        try:
            data['user_data'] = data.pop('user_id')
        except:
            return Response({"data":"true","status_code": 405, "message": "user_id does not exist"})
        # print(data['user_data'])

        try:
            user_details = BmsUser.objects.get(pk=data['user_data'])
            
        except BmsUser.DoesNotExist:
            return Response({'message': 'The User details do not exist'}, status=status.HTTP_404_NOT_FOUND)
        user_details_serializer = BmsUserSerializer_DeviceDetails(user_details)
        a = (user_details_serializer.data)
        # users = BmsUser.objects.filter(role_data__= user_role)

        # for user in users:
        #     print(user)
        
        # f= BmsSubAreaMasterSerializer()
        # print(a)

        user_devices_data = (a["user_data"]["role_id"]["device_data"])
        user_devices_data_list = []
        for i in user_devices_data:
            # print(i)
            if device_type == i['device_type']:
                user_devices_data_list.append(i)
        # print(user_devices_data_list)
        
        for i in user_devices_data_list:
            if i['device_type'] == device_type:
                sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__device_type=device_type,id=int(sub_area_id))
                for sub_area in sub_area_instances:
                    sub_area_name = sub_area.sub_area_name
                    # print(sub_area_name)
                    # tower_list = sub_area.area_data.floor_data.tower_data.id
                    data=  {
                                "id": sub_area.id,
                                "sub_area_name": sub_area.sub_area_name
                            }
                    device= sub_area.devices_details.filter(id=i['id']).values()        
                   
                    if not device:
                        pass
                    else:
                    # print(device,"me value hu")
                    # device_value = serializers.serialize('json',device)
                        devices_data.append(device)





        # a = list(set(tower_data))
        # subarea =  BmsSubAreaMaster.objects.filter(devices_details__device_type="AC")
        # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=17)
        # for i in user_devices_data_list:
            # print(i)
            # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__id=i)


        # sub_area_instances =  BmsSubAreaMaster.objects.filter(devices_details__device_type=device_type,id=int(sub_area_id))
        # for sub_area in sub_area_instances:
        #     sub_area_name = sub_area.sub_area_name
        #     # print(sub_area_name)
        #     # tower_list = sub_area.area_data.floor_data.tower_data.id
        #     data=  {
        #                 "sub_area_id": sub_area.id,
        #                 "sub_area_name": sub_area.sub_area_name
        #             }
        #     device= sub_area.devices_details.filter(device_type=device_type).values()        
                 
        #     # print(device,"me value hu")
        #     # device_value = serializers.serialize('json',device)
        #     devices_data.append(device)
        #     # devicea= (json.loads(device_value))    
        # subarea_data.append(data)
        

            
        # print(devices_data)
        # json_data = serializers.serialize('json', devices_data[0])
        # json.loads(json_data)
        
          
        return Response({"data":"true","status_code": 200, "message": " Devices Access list ","response":{"device_data":devices_data[0]}}, status=status.HTTP_200_OK)
             
#{ "user_id":2, "user_role" : "manager", "card_type" : "ac","sub_area_id":1}                    




@api_view(['GET'])
def UserTypeList(request):
    if request.method == 'GET':
        bms_users = BmsUserType.objects.filter(status="Active")
        bms_users_serializer = BmsUserTypeSerializer(bms_users, many=True)
        return Response({"data": "true", "status_code": 200, "message": "User Type Lists", "response": bms_users_serializer.data}, status=status.HTTP_200_OK)
    



@api_view(['POST'])
def get_device(request):
    if request.method == 'POST':
        data = request.data
        is_used= data["is_used"]
        device_status = data['status']
        device_type = data['device_type']
        bms_users = BmsDeviceInformation.objects.filter(device_type=device_type,is_used=is_used,status =device_status)
        bms_users_serializer = BmsDeviceInformationSerializer(bms_users, many=True)
        return Response({"data": "true", "status_code": 200, "message": "Device Lists", "response": bms_users_serializer.data}, status=status.HTTP_200_OK)
    
    
    
    
    
@api_view(['GET'])    
def geet(request):
    if request.method=='GET':    
        # Set the time limit in seconds
        time_limit = 4  # 1 hour

        # Define the data to be posted
        data =    {
                    
                    "module_name": "Inventory",
                    "module_slug": "Inventory",
                    "status": "Active"
                }

        # Set the URL of your Django API endpoint
        url = 'http://127.0.0.1:9999/manage_module_list'

        # Function to post data
        def post_data():
            try:
                # Send a POST request to the Django API
                response = requests.post(url, data=data)
                if response.status_code == 201:
                    print("Data posted successfully!")
                else:
                    print("Failed to post data. Status code:", response.status_code)
            except requests.exceptions.RequestException as e:
                print("An error occurred:", e)

        # Schedule the data posting
        schedule.every(1).seconds.do(post_data)
        # schedule.every(1).minute.do(post_data)


        schedule.every(10).minutes.do(post_data)

        # After every hour geeks() is called.
        schedule.every().hour.do(post_data)

        # Every day at 12am or 00:00 time bedtime() is called.
        schedule.every().day.at("00:00").do(post_data)

        # After every 5 to 10mins in between run work()
        schedule.every(5).to(10).minutes.do(post_data)

        # Every monday good_luck() is called
        schedule.every().monday.do(post_data)

        # Every tuesday at 18:00 sudo_placement() is called
        schedule.every().tuesday.at("18:00").do(post_data)


        # Start time
        start_time = time.time()

        # Loop until the time limit is reached
        while time.time() - start_time < time_limit:
            schedule.run_pending()
            time.sleep(1)

        print("Time limit reached. Exiting...")
        
        
    return Response({'msg':'success!!!'})