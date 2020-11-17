from django.shortcuts import render
from django.http import JsonResponse

#
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, Transfert
from .serializers import ClientSerializer, TransfertSerializer

# Create your views here.
def test(request):
    return JsonResponse({'key':'value'})


class TestView(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        clientsSerializer = ClientSerializer(clients, many=True)

        return Response(clientsSerializer.data)

class TransfertView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransfertSerializer
    def get(self, request, *args, **kwargs):
        return Response({'text':'transfert'})
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        # if not serializer.is_valid():
        #     return Response({'message':'invalid fields'})
        print('DATA', request.data)
        sender = serializer.validated_data['sender']
        receiver = serializer.validated_data['receiver']
        amount = serializer.validated_data['amount']
        method = serializer.validated_data['method']
        transferred = serializer.validated_data['transferred']
        # print('sender', sender, '\nreceiver', receiver, '\namount', amount)
        # transfert, created = Transfert.objects.get_or_create(user=user)
        return Response(
            {
                'sender':sender.username, 
                'receiver':receiver.username, 
                'method':method.get_name_display(), 
                'amount':amount,
                'transferred':transferred
            }
        )