from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import PersonSerializer
from .consumers import PersonConsumer


class PersonPostAPI(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'person_group',
                {'type': 'add_new_person'},
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
