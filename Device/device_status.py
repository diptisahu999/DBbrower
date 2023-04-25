from Device.models import bms_device_information
import json
from channels.consumer import SyncConsumer , AsyncConsumer
def getDeviceStatus():
    data = bms_device_information.objects.all()
    d_list = []
    for i in data:
        d = bms_device_information.objects.get(pk=int(i.pk))
        device_info = d.device_informations
        # device_info = json.loads(d.device_informations)
        print((device_info))
        if device_info is not None:
            d_list.append({
                "record_id":d.pk,
                "device_name":d.device_name,
                "is_dimmable":device_info["is_dimmable"] if "is_dimmable" in  device_info else None,
                "device_id": device_info["device_id"] if "device_id" in  device_info else None,
                "channel_id":device_info["channel_id"] if "channel_id" in device_info else None,
                "device_status": device_info["device_status"] if "channel_id" in device_info else None,
                "delay_second": "10"
            })
    Device_list   = json.dumps(d_list)
    return Device_list
    

