from channels.consumer import SyncConsumer , AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from Device.device_status import getDeviceStatus,getUserAreaCardList
from Device.device_control import ClientConfigSocket


class MyAsyncConsumer(SyncConsumer):
    connected_clients = set()
    def websocket_connect(self,event):
        # print("Websocket Connected...",event)
        user_id =3
        a = getUserAreaCardList(user_id)

        
        self.send({
                'type': 'websocket.accept',
            })
        self.send({
            'type': 'websocket.send',
            'text':  a,
            # "text": event['text']

        })
        # self.send({
        #     'type': 'websocket.send',
        #     'text':  event['text'],
        # })

        # websocket_receive
    def websocket_receive(self, event):
        # user_id =3
        # data= getUserAreaCardList(user_id)
        # self.send({
        #     "type": "websocket.send",
        #     "text": a,
        # })
        
        try : 
            data = json.loads(event['text'])
            print(data, "")
            ClientConfigSocket(data)
            user_id =3
            data= getUserAreaCardList(user_id)
            self.send_to_all(data, exclude=self)
            self.send({
            "type": "websocket.send",
            "text": data,
            })
            # self.send_to_all(data, exclude=self)
        except:
            user_id =3
            data= getUserAreaCardList(user_id)
            self.send({
            "type": "websocket.send",
            "text": data,
        })
             
       

        # self.send({
        #     "type": "websocket.send",
        #     "text": "Task finish",
        # })
       
    def send_to_all(self, message):
        print(message)
        for client in self.connected_clients:
            client.send({
                'type': 'websocket.send',
                'text': message,
            })

    def chat_message(self,event):
        print("data" ,event)
        # print("event .. " ,event['message'])
        self.send({ 
            'type':'websocket.send',
            'text': event['message']
        }
        )

    def websocket_disconnect(self,event):
        print("Websocket Disconnected...",event)
        raise StopConsumer()
    


    
class Connected(AsyncConsumer):
    async def websocket_connect(self,event):
        print("Websocket Connected...",event)
        await self.send({
                'type': 'websocket.accept',
            })
        await self.send({
            'type': 'websocket.send',
            'text': "Welcome to Broadview-innovations server",
        })

    async def websocket_disconnect(self,event):
        print("Websocket Disconnected...",event)
        raise StopConsumer()
    

class TesingFakeUrl(SyncConsumer):
    def websocket_connect(self,event):

        data = [
                    {
                        "id": 1,
                        "device_name": "Light",
                        "device_type": "LED",
                        "is_used": "No",
                        "device_informations": {
                        "is_dimmable": "true",
                        "isFan": "false",
                        "device_id": "3",
                        "channel_id": "18",
                        "device_status": "false",
                        "image_id": "2",
                        "delay_second": "0"
                        },
                        "status": "Active",
                        "create_at": "2023-05-01T13:13:34Z",
                        "updated_user_details_date": "2023-05-31T13:20:01.416498Z"
                    },
                    {
                        "id": 1,
                        "device_name": "Light",
                        "device_type": "LED",
                        "is_used": "No",
                        "device_informations": {
                        "is_dimmable": "true",
                        "isFan": "false",
                        "device_id": "3",
                        "channel_id": "18",
                        "device_status": "false",
                        "image_id": "2",
                        "delay_second": "0"
                        },
                        "status": "Active",
                        "create_at": "2023-05-01T13:13:34Z",
                        "updated_user_details_date": "2023-05-31T13:20:01.416498Z"
                    },
                    {
                        "id": 1,
                        "device_name": "Light",
                        "device_type": "LED",
                        "is_used": "No",
                        "device_informations": {
                        "is_dimmable": "true",
                        "isFan": "false",
                        "device_id": "3",
                        "channel_id": "18",
                        "device_status": "false",
                        "image_id": "2",
                        "delay_second": "0"
                        },
                        "status": "Active",
                        "create_at": "2023-05-01T13:13:34Z",
                        "updated_user_details_date": "2023-05-31T13:20:01.416498Z"
                    }
                    ]
        self.send({
                'type': 'websocket.accept',
            })
        self.send({
            'type': 'websocket.send',
            'text':  json.dumps(data),
            # "text": event['text']

        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": "msg receive",
        })

    def chat_message(self,event):
        # print("data" ,event)
        # print("event .. " ,event['message'])
        self.send({ 
            'type':'websocket.send'
        }
        )
    def websocket_disconnect(self,event):
        print("Websocket Disconnected...",event)
        raise StopConsumer()