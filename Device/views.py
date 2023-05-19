
from Device.models import *
from Device.serializers import *
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
# from django.http.response import StreamingHttpResponse
from Device.device_control import client_main_config
from django.http import HttpResponse
# from Device.camera import LiveWebCam


# import cv2

# # maskNet = load_model(os.path.join(settings.BASE_DIR,'face_detector/mask_detector.model'))

# class LiveWebCam(object):
# 	def __init__(self):
# 		self.url = cv2.VideoCapture("rtsp://admin:Admin@1234@192.168.1.248/cam/realmonitor?channel=1&subtype=1&authbasic=YWRtaW46QWRtaW4lNDAxMjM0")

# 	def __del__(self):
# 		cv2.destroyAllWindows()

# 	def get_frame(self):
# 		success,imgNp = self.url.read()
# 		resize = cv2.resize(imgNp, (640, 480), interpolation = cv2.INTER_LINEAR) 
# 		ret, jpeg = cv2.imencode('.jpg', resize)
# 		return jpeg.tobytes()

# building crud

@api_view(['GET', 'POST', 'DELETE'])
def building_list(request):
    if request.method == 'GET':
        building = BmsBuildingMaster.objects.all()
        building_serializer = ProfileSerializer(building, many=True)
        # building_serializer = BmsBuildingMasterSerializer(building, many=True) 
        return Response({"data":"true","status_code": 200, "message": "Building Lists", "response":building_serializer.data})
        
        
    elif request.method == 'POST':    
        building_serializer = BmsBuildingMasterSerializer(data=request.data)
        if building_serializer.is_valid(): 
            building_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Building Added Successfully", "response":building_serializer.data})
        return Response({"status_code":401,"responce":building_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = BmsBuildingMaster.objects.all().delete()
        return Response({'message': '{} Building Deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    
                                                                                                                                                                                                                            
@api_view(['GET', 'PUT', 'DELETE'])
def buildings(request, pk):
    try: 
        building = BmsBuildingMaster.objects.get(pk=pk) 
    except BmsBuildingMaster.DoesNotExist: 
        return Response({'message': 'Building does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        building_serializer = ProfileSerializer(building)
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":building_serializer.data}) 
 
    elif request.method == 'PUT':  
        building_serializer = BmsBuildingMasterSerializer(building, data=request.data) 
        if building_serializer.is_valid(): 
            building_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Building Updated Successfully", "response":building_serializer.data})
            
        return Response({"status_code":401,"responce":building_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        building.delete() 
        return Response({'message': 'Building was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# Bms_floor_master crud

@api_view(['GET', 'POST', 'DELETE'])
def floor_list(request):
    if request.method == 'GET':
        Floors = BmsFloorMaster.objects.all()
        Floors_serializer = BmsFloorMasterSerializer(Floors, many=True,read_only=True)
        return Response({"data":"true","status_code": 200, "message": "Floor Lists", "response":Floors_serializer.data})
              
    elif request.method == 'POST':
       
        data = request.data
        tower_ids = data['tower_id']
        for tower_id in tower_ids:
            tower = dict(data)
            tower.update({'tower_id': tower_id})
            print(tower)
            serializer = BmsFloorMasterSerializerPost(data=tower)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'data': 'true', 'status_code': 200, 'message': 'Data added successfully'})
    
    elif request.method == 'DELETE':
        count = BmsFloorMaster.objects.all().delete()
        return Response({'message': '{} Floor was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def floor_details(request, pk):
    try: 
        Floors = BmsFloorMaster.objects.get(pk=pk) 
    except BmsFloorMaster.DoesNotExist: 
        return Response({'message': 'Floor does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        Floors_serializer = BmsFloorMasterSerializer(Floors) 
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":Floors_serializer.data}) 
 
    elif request.method == 'PUT': 
        Floors_serializer = BmsFloorMasterSerializerPost(Floors, data=request.data) 
        if Floors_serializer.is_valid(): 
            Floors_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Floor Updated Successfully", "response":Floors_serializer.data})
            
        return Response({"status_code":401,"responce":Floors_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        Floors.delete() 
        return Response({'message': 'Floor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)





#Bms_Deperament_master crud


@api_view(['GET', 'POST', 'DELETE'])
def department_list(request):
    if request.method == 'GET':
        department = BmsDepartmentMaster.objects.all()
        department_serializer =  BmsDepartmentMasterSerializer(department, many=True)
        return Response({"data":"true","status_code": 200, "message": "Department lists", "response":department_serializer.data})
    
    elif request.method == 'POST':
        department_serializer = BmsDepartmentMasterSerializerPost(data=request.data)
        if department_serializer.is_valid():
            department_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Department Added Successfully", "response":department_serializer.data}) 
        return Response({"status_code":401,"responce":department_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count =  BmsDepartmentMaster.objects.all().delete()
        return Response({'message': '{} Department was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def department(request, pk):
    try: 
        departments = BmsDepartmentMaster.objects.get(pk=pk) 
    except BmsDepartmentMaster.DoesNotExist: 
        return Response({'message': 'The Department does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        departments_serializer =  BmsDepartmentMasterSerializer(departments) 
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":departments_serializer.data}) 
 
    elif request.method == 'PUT':  
        departments_serializer = BmsDepartmentMasterSerializerPost(departments, data=request.data) 
        if departments_serializer.is_valid(): 
            departments_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Department Update Successfully", "response":departments_serializer.data})
            
        return Response({"status_code":401,"responce":departments_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        departments.delete() 
        return Response({'message': 'Department was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
    
    
# Bms_sub_area_master crud

@api_view(['GET', 'POST', 'DELETE'])
def bms_sub_area_list(request):
    if request.method == 'GET':
        subare = BmsSubAreaMaster.objects.all()
        subarea_serializer = BmsSubAreaMasterSerializer(subare, many=True)
        return Response({"data":"true","status_code": 200, "message": "Sub Area Lists", "response":subarea_serializer.data})
        
        
    elif request.method == 'POST':
       
        data = request.data
        Floor_ids = data['area_data']
        print(Floor_ids)
        for Floor_id in Floor_ids:
            floor = dict(data)
            floor.update({'area_data': Floor_id})
            # print(floor)    
            serializer = BmsSubAreaMasterSerializerPost(data=floor)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'data': 'true', 'status_code': 200, 'message': 'Data added successfully'}) 
        # return Response({"data":"true","status_code": 200, "message": "Building Added Successfully", "response":building_serializer.data})
         
    elif request.method == 'DELETE':
        count = BmsSubAreaMaster.objects.all().delete()
        return Response({'message': '{} Sub Area was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    

@api_view(['GET', 'PUT', 'DELETE'])
def bms_sub_area(request, pk):
    try: 
        subarea = BmsSubAreaMaster.objects.get(pk=pk) 
    except BmsSubAreaMaster.DoesNotExist: 
        return Response({'message': 'The Sub Area does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        subarea_serializer =  BmsSubAreaMasterSerializer(subarea) 
        return JsonResponse({"data":"true","status_code": 200, "message": "Get data Successfully", "response":subarea_serializer.data}) 
 
    
    elif request.method == 'PUT': 
        data = request.data
        Floor_ids = data['devices_details']

        for device_id in Floor_ids:
            devices = BmsDeviceInformation.objects.get(pk=device_id['id'])
            devices_serializer = BmsDeviceInformationSerializer(devices, data=device_id)
            if devices_serializer.is_valid():
                devices_serializer.save()
            else:
                return Response({"status_code": 400, "response": devices_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        subarea_serializer = BmsSubAreaMasterSerializer(subarea, data=request.data) 
        if subarea_serializer.is_valid(): 
            subarea_serializer.save() 
            return Response({"data": "true", "status_code": 200, "message": "Sub Area Update Successfully", "response": subarea_serializer.data})

        return Response({"status_code": 401, "response": subarea_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE': 
        subarea.delete() 
        return Response({'message': 'Sub Area was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
# Bms_locker crud
    

@api_view(['GET', 'POST', 'DELETE'])
def bms_locker_list(request):
    if request.method == 'GET':
        lockers = BmsLocker.objects.all()
        lockers_serializer = BmsLockerSerializer(lockers, many=True)
        return Response({"data":"true","status_code": 200, "message": "Locker lists", "response":lockers_serializer.data})
        
        
        
    elif request.method == 'POST':
        lockers_serializer = BmsLockerSerializerPost(data=request.data)
        if lockers_serializer.is_valid():
            lockers_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Locker Added Successfully", "response":lockers_serializer.data})     
        return Response({"status_code":401,"responce":lockers_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        count = BmsLocker.objects.all().delete()
        return Response({'message': '{} Locker was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def bms_locker_list_details(request, pk):
    try: 
        lockers = BmsLocker.objects.get(pk=pk) 
    except BmsLocker.DoesNotExist: 
        return Response({'message': 'The Locker does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        lockers_serializer = BmsLockerSerializer(lockers) 
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":lockers_serializer.data}) 
 
    elif request.method == 'PUT':
        lockers_serializer = BmsLockerSerializerPost(lockers, data=request.data) 
        if lockers_serializer.is_valid(): 
            lockers_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Locker Update Successfully", "response":lockers_serializer.data})
            
        return Response({"status_code":401,"responce":lockers_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        lockers.delete() 
        return Response({'message': 'Locker was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)




# Device API LIST

@api_view(['GET', 'POST','DELETE'])
def device_list(request):
    if request.method == 'GET':
        devices = BmsDeviceInformation.objects.all()
        devices_serializer = BmsDeviceInformationSerializer(devices, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "Device Information Lists", "response":devices_serializer.data})       
        
    elif request.method == 'POST':
        devices_serializer = BmsDeviceInformationSerializerPost(data=request.data)
        if devices_serializer.is_valid():
            devices_serializer.save()
            # print(tutorial_serializer.data)
            return Response({"data":"true","status_code": 200, "message": "Device Information Added Successfully!", "response":devices_serializer.data}) 
        return Response({"status_code":401,"responce":devices_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        count = BmsDeviceInformation.objects.all().delete()
        return Response({'message': '{} Device information was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    
    


@api_view(['GET', 'PUT', 'DELETE'])
def device_list_details(request, pk):
    try: 
        devices = BmsDeviceInformation.objects.get(pk=pk) 
    except BmsDeviceInformation.DoesNotExist: 
        return Response({'message': 'The device information does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        devices_serializer = BmsDeviceInformationSerializer(devices) 
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":devices_serializer.data}) 
 
    elif request.method == 'PUT':
        devices_serializer = BmsDeviceInformationSerializerPost(devices, data=request.data) 
        if devices_serializer.is_valid(): 
            devices_serializer.save() 
            client_main_config()
            return Response({"data":"true","status_code": 200, "message": "Device Information Successfully", "response":devices_serializer.data})
            
        return Response({"status_code":401,"responce":devices_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        devices.delete() 
        return Response({'message': 'Device information was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

# Area master crud

@api_view(['GET', 'POST', 'DELETE'])
def bms_area_list(request):
    if request.method == 'GET':
        areas = BmsAreaMaster.objects.all()
        areas_serializer = BmsAreaMasterSerializer(areas, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "Area Lists", "response":areas_serializer.data})
      
    elif request.method == 'POST':
       
        data = request.data
        area_ids = data['floor_data']
        # print(Floor_ids)
        for area_id in area_ids:
            area = dict(data)
            area.update({'floor_data': area_id})
            # print(area)    
            serializer = BmsAreaMasterSerializerPost(data=area)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'data': 'true', 'status_code': 200, 'message': 'Data added successfully'})  
        
    # elif request.method == 'POST':
    #     areas_serializer = BmsAreaMasterSerializerPost(data=request.data)
    #     if areas_serializer.is_valid():
    #         areas_serializer.save()
    #         return Response({"data":"true","status_code": 200, "message": "Area Added Successfully", "response":areas_serializer.data})    
    #     return Response({"status_code":401,"responce":areas_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        count = BmsAreaMaster.objects.all().delete()
        return Response({'message': '{} Area were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    



@api_view(['GET', 'PUT', 'DELETE'])
def bms_area_list_1(request, pk):
    try: 
        areas = BmsAreaMaster.objects.get(pk=pk) 
    except BmsAreaMaster.DoesNotExist: 
        return Response({'message': 'The area does not exist',"status_code": 404}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        areas_serializer = BmsAreaMasterSerializer(areas) 
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":areas_serializer.data}) 
 
    elif request.method == 'PUT':  
        areas_serializer = BmsAreaMasterSerializerPost(areas, data=request.data) 
        if areas_serializer.is_valid(): 
            areas_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Area Update Successfully", "response":areas_serializer.data})
            
        return Response({"status_code":401,"responce":areas_serializer.errors},status=status.HTTP_400_BAD_REQUEST)  
 
    elif request.method == 'DELETE': 
        areas.delete() 
        return Response({'response': 'Area was deleted successfully!',"status_code": 200}, status=status.HTTP_204_NO_CONTENT)
    


# BMS_USER_AREA_CARD_LIST


@api_view(['GET', 'POST', 'DELETE'])
def bms_user_area_card_list(request):
    if request.method == 'GET':
        area_card = BmsUserAreaCardsList.objects.all()    
        area_card_serializer = BmsUserAreaCardsListSerializer(area_card, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": 200, "message": "User Card Lists", "response":area_card_serializer.data})
        
        
    elif request.method == 'POST':
        area_card_serializer = BmsUserAreaCardsListSerializer(data=request.data)
        if area_card_serializer.is_valid():
            area_card_serializer.save()
            return Response({"data":"true","status_code": 200, "message": "Card Added Successfully", "response":area_card_serializer.data})
            
        return Response({"status_code":401,"responce":area_card_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = BmsUserAreaCardsList.objects.all().delete()
        return Response({'message': '{} Card was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    





@api_view(['GET', 'PUT', 'DELETE'])
def bms_user_area_card_list_details(request, pk):
    try: 
        area_card = BmsUserAreaCardsList.objects.get(pk=pk) 
    except BmsUserAreaCardsList.DoesNotExist: 
        return Response({'message': 'The card does not exist',"status_code": 404}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        area_card_serializer = BmsUserAreaCardsListSerializer(area_card) 
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":area_card_serializer.data}) 
 
    elif request.method == 'PUT': 
        area_card_serializer = BmsUserAreaCardsListSerializer(area_card, data=request.data) 
        if area_card_serializer.is_valid(): 
            area_card_serializer.save() 
            return Response({"data":"true","status_code": 200, "message": "Card Update Successfully", "response":area_card_serializer.data})
            
        return Response({"status_code":401,"responce":area_card_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE': 
        area_card.delete() 
        return Response({'response': 'Card was deleted successfully!',"status_code": 200}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    
 ## bms_device_type_master
    
@api_view(['GET','POST','DELETE'])
def Bms_device_type_master_list(request):
    if request.method=='GET':
        devices=BmsDeviceTypeMaster.objects.all()
        device_serialiser=BmsDeviceTypeMasterSerializer(devices,many=True)
        return Response({"data":"true","status_code": 200, "message": "Device type lists", "response":device_serialiser.data})
        
    elif request.method=='POST':
        device_serialisers=BmsDeviceTypeMasterSerializer(data=request.data)
        if device_serialisers.is_valid():
            device_serialisers.save()
            return Response({"data":"true","status_code": 200, "message": "Device type Updated Successfully", "response":device_serialisers.data})
        else:
            return Response({"status_code":401,"responce":device_serialisers.errors},status=status.HTTP_400_BAD_REQUEST) 
        
    elif request.method=='DELETE':
        count=BmsDeviceTypeMaster.objects.all().delete()
        return Response({'message': '{} device type were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET','PUT','DELETE'])
def bms_device_type_master_details(request,self,pk):
    try:
        device=BmsDeviceTypeMaster.objects.get(pk=pk)
    except BmsDeviceTypeMaster.DoesNotExist:
        return Response({'message': 'device type does not exist',"status_code": 404}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        devicee_serializer=BmsDeviceTypeMasterSerializer(device)
        return Response({"data":"true","status_code": 200, "message": "Get data Successfully", "response":devicee_serializer.data})
        
    elif request.method=='PUT':
        device_serializers=BmsDeviceTypeMasterSerializer(device,data=request.data)
        if device_serializers.is_valid():
            device_serializers.save()
            return Response({"data":"true","status_code": 200, "message": "Bulding Updated Successfully", "response":device_serializers.data})      
        return Response({"status_code":401,"responce":device_serializers.errors},status=status.HTTP_400_BAD_REQUEST) 
 
 
    elif request.method=='DELETE':
        device.delete()
        return Response({'response': 'Device type deleted successfully!',"status_code": 200}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET','POST','DELETE'])
def bms(request):
    if request.method=='GET':
         bms=BmsAreaMaster.objects.all()
         serializer=BmsAreaMasterSerializer(bms,many=True)
         return Response(serializer.data)
     
     
    elif request.method=='POST':
        serializer=BmsAreaMasterSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status_code':200,'msg':'data added succesfully!!!','responce':serializer.data})
        return Response({'status_code':401,'msg':'data does not post!!!','responce':serializer.errors})
    
    
    elif request.method=='DELETE':
        bms=BmsAreaMaster.objects.all()
        bms.delete()
        return Response({'msg':'data delete successfully!!!!'})
    
    
@api_view(['GET','PUT','DELETE'])
def Bms(request,pk):
    try:
        bmss=BmsAreaMaster.objects.get(pk=pk)
    except BmsAreaMaster.DoesNotExist:
        return Response({'msg':'data does not exit'})
    
    
    if request.method=='GET':
        serializer=BmsAreaMasterSerializer(bmss)
        return Response({'msg':'get data succesfully!!!','responce':serializer.data})
    
    
    elif request.method=='PUT':
        dd=BmsAreaMaster.objects.get(pk=pk)
        abc=BmsAreaMaster.objects.filter(pk=pk)
        serializers=BmsAreaMasterSerializer(abc,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status':'true','msg':'data update succesfully!!!','status':200,'responce':serializers.data})
        
        return Response({'msg':'data does not exist!!!','responce':serializers.errors})
    
    
    elif request.method=='DELETE':
        bmss.delete()
        return Response({'msg':'data delete succesfully!!!!'})
        