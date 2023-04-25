a = [{"record_id": 1, "device_name": "Entry", "device_id": "61", "channel_id": "1", "device_status": "false"}, {"record_id": 2, "device_name": "IT workspace", "device_id": "61", "channel_id": "13", "device_status": "true"}]


# for i in a:
#     if i['device_status'] =="true":
#         param={"device_id":int(i.get('device_id')),
#         "channel_id":int(i.get('channel_id')),
#         "device_status":str(i.get("device_status"))}
#         print(param)
#     if i['device_status'] =="false":
#         param={"device_id":int(i.get('device_id')),
#         "channel_id":int(i.get('channel_id')),
#         "device_status":str(i.get("device_status"))}
#         print(param)
a = [1,2,4]
b =[5,6]
for i in b:
    a.append(i)
print(a)