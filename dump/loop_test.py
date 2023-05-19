# a ={"isFan": "false", "is_dimmable": "false", "device_id": "61", "channel_id": "1", "image_id": "1", "device_status": "false", "delay_second": "0"}
# if "device_id" in a:
#     print(a["device_id"])
import binascii
a = b'\xc0\xa8\x01\xc8SMARTCLOUD\xaa\xaa\x14\x017\x00 \xef\xff\xff\xff\x01\xfe0\xff\x8f\x03\x00\x00\x00\x81;'
a = (a.hex())
device_id = a[:2]
device_id = int(device_id, 16)
print(str(device_id))

