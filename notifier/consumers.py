from channels.generic.websocket import WebsocketConsumer,AsyncConsumer,AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync




# class NoseyConsumer(AsyncJsonWebsocketConsumer):

#     def connect(self):
#         print("====================connected=====================")
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         print(text_data)

#         message="hellooooo john"
#         self.send(text_data=json.dumps({
#             'message': message
#         }))


# class NoseyConsumer(AsyncConsumer):

#     async def websocket_connect(self, event):
#         print(self.channel_name)
#         await self.send({
#             "type": "websocket.accept",
#         })

#     async def websocket_receive(self, event):
#         await self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })
class NotificationConsumer(WebsocketConsumer):
    
    def connect(self):
       # Checking if the User is logged in
        if self.scope["user"].is_anonymous:
            # Reject the connection
            self.close()
        else:
            # print(self.scope["user"])   # Can access logged in user details by using self.scope.user, Can only be used if AuthMiddlewareStack is used in the routing.py
            self.group_name = "noti"  # Setting the group name as the pk of the user primary key as it is unique to each user. The group name is used to communicate with the user.
            print(self.channel_name)
            print(self.scope["user"].email)
            async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
            self.accept()

    # Function to disconnet the Socket
    def disconnect(self, close_code):
        self.close()
        # pass

    # Custom Notify Function which can be called from Views or api to send message to the frontend
    def notify(self, event):
        self.send(text_data=json.dumps(event["text"]))