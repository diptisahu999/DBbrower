from Device.models import BmsDeviceInformation
import json
# from channels.consumer import SyncConsumer , AsyncConsumer
# 
d_list = []

def getDeviceStatus():
    data = BmsDeviceInformation.objects.all()
    d_list.clear()
    for i in data:
        # print(i)
        d = BmsDeviceInformation.objects.get(pk=int(i.pk))
        # print(d)        
        device_info = d.device_informations
        dump = []
        print(device_info)
        # device_info = json.loads(d.device_informations)
        if device_info is not None:
            # print(device_info)
            if str(d.device_type) == "LED":
                dump = {
                    "record_id": d.pk,
                    "device_name": d.device_name,
                    "device_type": d.device_type ,
                    "is_dimmable": device_info["is_dimmable"] if "is_dimmable" in device_info else None,
                    "device_id": device_info["device_id"] if "device_id" in device_info else None,
                    "channel_id": device_info["channel_id"] if "channel_id" in device_info else None,
                    "device_status": device_info["device_status"] if "channel_id" in device_info else None,
                    "delay_second": "10"
                }
               
                # {'device_id': '92', 'channel_id': '0', 'ac_temp': '23', 'rm_temp': '34', 'mode': 'C', 'swing': '', 'fspeed': 'H', 'device_status': 'false'}
            elif str(d.device_type) == "AC":
                dump = {
                    "record_id": d.pk,
                    "device_name": d.device_name,
                    "device_type": d.device_type ,
                    'device_id':  device_info["device_id"] if "device_id" in device_info else None,
                    'channel_id':  device_info["channel_id"] if "channel_id" in device_info else None,
                    'ac_temp':  device_info["ac_temp"] if "ac_temp" in device_info else None,
                    'rm_temp':  device_info["rm_temp"] if "rm_temp" in device_info else None,
                    'mode':  device_info["mode"] if "mode" in device_info else None,
                    'swing':  device_info["swing"] if "swing" in device_info else None,
                    'fspeed':  device_info["fspeed"] if "fspeed" in device_info else None,
                    'device_status':  device_info["device_status"] if "device_status" in device_info else None,
                    }
                
            d_list.append(dump)
    Device_list = json.dumps(d_list)
    return Device_list
