from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes
)

from rest_framework import (
    viewsets,
    mixins,
    status
)

from client.models import (
    Client
)

from client import serializers

@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'id',
                OpenApiTypes.STR,
                description='CIDs to filter a client',
            )
        ]
    )
)
class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientSerializer
    queryset = Client.objects.all()
    
    """ Consulta de cliente por su ud """
    def get_queryset(self):
        client_id = int(self.request.query_params.get('id', 0))
        
        return self.queryset.filter(id=client_id)