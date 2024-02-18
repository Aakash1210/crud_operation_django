from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import NetworkAdmin, Router
from .serializers import NetworkAdminSerializer, RouterSerializer

class NetworkAdminViewSet(viewsets.ModelViewSet):
    queryset = NetworkAdmin.objects.all()
    serializer_class = NetworkAdminSerializer

class RouterViewSet(viewsets.ModelViewSet):
    queryset = Router.objects.filter(is_deleted=False)
    serializer_class = RouterSerializer

    @action(detail=True, methods=['GET'])
    def get_router(self, request, pk=None):
        router = self.get_object()
        serializer = self.get_serializer(router)
        return Response(serializer.data)

    @action(detail=True, methods=['PUT'])
    def update_router(self, request, pk=None):
        router = self.get_object()
        serializer = self.get_serializer(router, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['DELETE'])
    def delete_router(self, request, pk=None):
        router = self.get_object()
        router.is_deleted = True
        router.save()
        return Response({'detail': 'Router soft-deleted successfully.'})

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
