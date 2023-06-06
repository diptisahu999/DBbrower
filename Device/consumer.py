from channels.consumer import SyncConsumer , AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from Device.device_status import getDeviceStatus,getUserAreaCardList
from Device.device_control import ClientConfigSocket
from channels.consumer import SyncConsumer , AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync


class MyAsyncConsumer(SyncConsumer):
    connected_clients = set()
    def websocket_connect(self,event):
        # print("Websocket Connected...",event)
        user_id =24
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
            user_id =24
            data= getUserAreaCardList(user_id)
            self.send_to_all(data, exclude=self)
            self.send({
            "type": "websocket.send",
            "text": data,
            })
            # self.send_to_all(data, exclude=self)
        except:
            user_id =24
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
    



class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.group_name = self.scope['url_route']['kwargs']['groupnuname']
        user_id = int(self.group_name)
        a = getUserAreaCardList(user_id)
        # print("Websocket Connected...",event)
        # print("Channel layer " , self.channel_layer) #get default channel layer
        # print("Channel name " , self.channel_name) #get default channel name



        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)     #convert async function to sync funtion
        self.send({
            'type':'websocket.accept'
        })
        async_to_sync(self.channel_layer.group_send)(
                self.group_name,{
                'type':'chat.message',
                'message': a
                }
            )

    def websocket_receive(self,event):
        self.group_name = self.scope['url_route']['kwargs']['groupnuname']
        user_id = int(self.group_name)
        try:
            data = json.loads(event['text'])
            print(data, "")
            ClientConfigSocket(data)
            data= getUserAreaCardList(user_id)
            print(type(data))
            # self.group_name = self.scope['url_route']['kwargs']['groupnuname']
            # print("Group name: ",self.group_name)

            async_to_sync(self.channel_layer.group_send)(
                self.group_name,{
                'type':'chat.message',
                'message': data
                }
            )
        except:
                async_to_sync(self.channel_layer.group_send)(
                self.group_name,{
                'type':'chat.message',
                'message': "device informations wrong"
                }
            )


    def chat_message(self,event):
        # print("data" ,event)
        # print("event .. " ,event['message'])
        self.send({ 
            'type':'websocket.send',
            'text': event['message']
        }
        )

    def websocket_disconnect(self,event):
        print("Websocket Disconnected...",event)
        print("Channel layer " , self.channel_layer) #get default channel layer
        print("Channel name " , self.channel_name) #get default channel name
        async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)
        raise StopConsumer()