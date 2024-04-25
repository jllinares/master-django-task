import logging

from rest_framework.response import Response
from client import serializers

from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema
)
from rest_framework import (
    viewsets,
    status
)
from client.models import (
    Client
)


# Configuración del logger
logger = logging.getLogger("API")

@extend_schema_view(
    list=extend_schema(description="Obtener lista de clientes"),
    retrieve=extend_schema(description="Obtener a un cliente"),
    create=extend_schema(description="Crear un nuevo cliente."),
    update=extend_schema(description="Actualizar completamente a un cliente"),
    partial_update=extend_schema(description="Actualizar parcialmente a un cliente"),
    destroy=extend_schema(description="Borrar un cliente")
)

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientSerializer
    queryset = Client.objects.all()
    
    """ Creacion de usuario """
    def create(self, request, *args, **kwargs):
        logger.info("Consultando al cliente")
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    """ Actualizacion de usuario """
    @extend_schema(description="Actualización completa de un cliente existente")
    def update(self, request, *args, **kwargs):
        logger.info("Actualizando al cliente")
        
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    """ Actualizacion de usuario """
    def partial_update(self, request, *args, **kwargs):
        logger.info("Actualizando parcialmente cliente")
        
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_data = serializer.validated_data
        
        # Actualizamos solo los campos enviados
        for key, value in updated_data.items():
            setattr(instance, key, value)
       
        instance.save()        
        
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
