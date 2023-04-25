from django.shortcuts import render
from Device.models import *
from Device.serializers import *
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from Device.device_control import client_main_config
from Device.device_status import getDeviceStatus
from . import consumer
import requests,socket
import json


@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = bms_building_master.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = Bms_Bulding_master_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "Login Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = Bms_Bulding_master_Serializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
           
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return Response({"data":"true","status_code": 200, "message": "Data added Successfully", "response":tutorial_serializer.data})
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = bms_building_master.objects.all().delete()
        return JsonResponse({'message': '{} data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def user(request, pk):
    try: 
        tutorial = bms_building_master.objects.get(pk=pk) 
    except bms_building_master.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_Bulding_master_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_Bulding_master_Serializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



#Bms_floor_master crud

@api_view(['GET', 'POST', 'DELETE'])
def floor_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = bms_floor_master.objects.all()
        # tower_id=Bms_Bulding_master_Serializer(many=True,read_only=True)
        title = request.GET.get('tower_id', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        tutorials_serializer = Bms_floor_serializer(tutorials, many=True,read_only=True)
        
# Bms_floor_serializer
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        # print(tutorial_data)
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = Bms_floor_master_Serializer_post(data=tutorial_data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return Response({"data":"true","status_code": 200, "message": "Data added Successfully", "response":tutorial_serializer.data})
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = bms_floor_master.objects.all().delete()
        return JsonResponse({'message': '{} data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def floor_details(request, pk):
    try: 
        tutorial = bms_floor_master.objects.get(pk=pk) 
    except bms_floor_master.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_floor_serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_floor_master_Serializer_post(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
#Bms_Deperament_master crud
@api_view(['GET', 'POST', 'DELETE'])
def department_list(request):
    if request.method == 'GET':
        tutorials = bms_department_master.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        tutorials_serializer = Bms_department_master_Serializer(tutorials, many=True)
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorials_serializer.data})
    
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = Bms_department_master_Serializer_post(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Data added Successfully", "response":tutorial_serializer.data}) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = bms_department_master.objects.all().delete()
        return JsonResponse({'message': '{} data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def department(request, pk):
    try: 
        tutorial = bms_department_master.objects.get(pk=pk) 
    except bms_department_master.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_department_master_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_department_master_Serializer_post(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
    
    
# Bms_sub_area_master crud
@api_view(['GET', 'POST', 'DELETE'])
def Bms_sub_area_list(request):
    if request.method == 'GET':
        tutorials = bms_sub_area_master.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        tutorials_serializer = Bms_sub_area_master_Serializer(tutorials, many=True)
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorials_serializer.data})
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = Bms_sub_area_master_Serializer_post(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Data added Successfully", "response":tutorial_serializer.data})
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = bms_sub_area_master.objects.all().delete()
        return JsonResponse({'message': '{} data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    

@api_view(['GET', 'PUT', 'DELETE'])
def Bms_sub_area(request, pk):
    try: 
        tutorial = bms_sub_area_master.objects.get(pk=pk) 
    except bms_sub_area_master.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_sub_area_master_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_sub_area_master_Serializer_post(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
# Bms_locker crud
    

@api_view(['GET', 'POST', 'DELETE'])
def Bms_locker_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = bms_locker.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = Bms_locker_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = Bms_locker_Serializer_post(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Data added Successfully", "response":tutorial_serializer.data})
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = bms_locker.objects.all().delete()
        return JsonResponse({'message': '{} data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def Bms_locker_list_details(request, pk):
    try: 
        tutorial = bms_locker.objects.get(pk=pk) 
    except bms_locker.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_locker_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_locker_Serializer_post(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# Device API LIST

@api_view(['GET', 'POST', 'PUT','DELETE'])
def Device_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = bms_device_information.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = Bms_Devices_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = Bms_Devices_Serializer_post(data=tutorial_data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return Response({"data":"true","status_code": 200, "message": "Data added Successfully", "response":tutorial_serializer.data}) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = bms_device_information.objects.all().delete()
        return JsonResponse({'message': '{} data were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    
    


@api_view(['GET', 'PUT', 'DELETE'])
def Device_list_details(request, pk):
    try: 
        tutorial = bms_device_information.objects.get(pk=pk) 
    except bms_device_information.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_Devices_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_Devices_Serializer_post(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            client_main_config()
            getDeviceStatus()
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def bms_building_floor_area_subarea_device_Serializer_list(request):
    if request.method == 'GET':
        tutorials = bms_sub_area_master.objects.all()
        tutorials_serializer = bms_building_floor_area_subarea_device_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
    

#bms_area API


@api_view(['GET', 'POST', 'DELETE'])
def bms_area_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = bms_area_master.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = bms_area_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = bms_area_Serializer_post(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Data added Successfully", "response":tutorial_serializer.data})
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = bms_area_Serializer.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def bms_area_list_1(request, pk):
    try: 
        tutorial = bms_area_master.objects.get(pk=pk) 
    except bms_area_master.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist',"status_code": 404}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = bms_area_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = bms_area_Serializer_post(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'response': 'data was deleted successfully!',"status_code": 200}, status=status.HTTP_204_NO_CONTENT)
    


#BMS_USER_AREA_CARD_LIST


@api_view(['GET', 'POST', 'DELETE'])
def bms_user_area_card_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = bms_user_area_cards_List.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = bms_user_area_cards_List_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = bms_user_area_cards_List_Serializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return Response({"data":"true","status_code": 200, "message": "Data added Successfully", "response":tutorial_serializer.data})
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = bms_area_Serializer.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    



@api_view(['GET', 'PUT', 'DELETE'])
def bms_user_area_card_list_details(request, pk):
    try: 
        tutorial = bms_user_area_cards_List.objects.get(pk=pk) 
    except bms_user_area_cards_List.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist',"status_code": 404}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = bms_user_area_cards_List_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": 200, "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = bms_user_area_cards_List_Serializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'response': 'data was deleted successfully!',"status_code": 200}, status=status.HTTP_204_NO_CONTENT)