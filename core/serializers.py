from rest_framework import serializers
from .models import Client, Transfert


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client 
        fields = (
            'name',
            'email',
            'phone',
        )

class TransfertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfert
        fields = (
            'sender',
            'receiver',
            'amount',
            'method',
            'transferred'
        )