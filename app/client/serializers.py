from rest_framework import serializers
from client.models import (
    Client
)

#Serializadores

#Serializado del cliente
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'age', 'country', 'active', 'creation_date']
        read_only_fields = ['id', 'creation_date']