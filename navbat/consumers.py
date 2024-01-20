import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Person
from .serializers import PersonSerializer


class PersonConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("person_group", self.channel_name)
        await self.send_initial_person_list()

    async def send_initial_person_list(self):
        person_list = await self.get_person_list()
        await self.send(text_data=json.dumps(person_list))

    @sync_to_async
    def get_person_list(self):
        person_list = Person.objects.all()
        serializer = PersonSerializer(person_list, many=True)
        return serializer.data

    async def add_new_person(self, event):
        await self.send_initial_person_list()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("person_group", self.channel_name)
