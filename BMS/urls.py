from django.contrib import admin
from django.urls import path, include
import threading
from socket import *
# import socket
import requests
import json
from Authenticate import views
import public_ip as ip
from django.shortcuts import render
from getmac import get_mac_address as gma

try:
    s = socket(AF_INET,SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = (s.getsockname()[0])
    # print("my public ip: ",ip.get())
    # macaddr = gma().upper()
    # url = "http://bms.bi-team.in/api/licenseKeyStored"
    # headers = {'Content-type': 'application/json', 'Accept': '*/*','Connection':'keep-alive','Accept-Encoding':'gzip, deflate, br','User-Agent':'PostmanRuntime/7.32.2',"Access-Control-Allow-Origin":''}
    # get_auth_token= {
    # "license_key":"BI25052023",
    # "mac_address":str(macaddr),
    # "ip_address":str(ip_address),
    # }
    # t = requests.post(url, json=get_auth_token ,headers = headers)
    # res = json.loads(t.text)
    # print(res['status'])
    s=socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    m=socket(AF_INET, SOCK_DGRAM)
    m.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    m.bind(('0.0.0.0', 6000))
except:
    print ("Socket Error")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Authenticate.urls')),
    path('', include('Device.urls')),
    # path('',include('Inventory.urls')),
    path('', include('Camera.urls')),
]





# print(myip)
# def index(request):
#     if request.method == 'POST':
#         input_text = request.POST.get('input-text')
#         print(input_text)
#         url = "http://tracker.bi-team.in/api/index.php"
#         headers = {'Content-type': 'application/json', 'Accept': '*/*', 'Connection': 'keep-alive',
#                    'Accept-Encoding': 'gzip, deflate, br', 'User-Agent': 'PostmanRuntime/7.32.2', "Access-Control-Allow-Origin": ''}
#         get_auth_token = {
#             "user_id": '2',
#             "license_key": str(input_text),
#             "mac_address": str(macaddr),
#             "ip_address": str(ip.get()),
#             "action": 'add_license_information'
#         }
#         t = requests.post(url, json=get_auth_token, headers=headers)
#         res = json.loads(t.text)
#         if res['status'] == "True":
#             urlpatterns =[]
#             url_list = [path('', include('Authenticate.urls')),
#                         path('', include('Device.urls')),]
#             for i in url_list:
#                 urlpatterns.append(i)
#             my_variable = "Login Succesfully"
#             return render(request, 'loginSuccess.html', {'my_variable': my_variable})

#         else:
#             my_variable = "Login Unsuccesfull"
#             urlpatterns = [
#                         path('', index, name ='index'),]
#             return render(request, 'Loginfail.html', {'my_variable': my_variable})

#         # Do something with the input_text value
#     return render(request, 'index.html')


# device_control.main_config()
# jsonUpdator = threading.Thread(target=device_control.client_main_config())
# jsonUpdator.start()
# device_control.client_main_config()
# threading.Thread(target=device_status.getDeviceStatus())

# device_status.getDeviceStatus()