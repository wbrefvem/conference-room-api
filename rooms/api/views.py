from rest_framework import viewsets
from rooms import models
from rooms.api import serializers, renderers


class BaseViewSet(viewsets.ModelViewSet):
    renderer_classes = (renderers.JSONRenderer,)


class BuildingViewSet(BaseViewSet):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer


class RoomViewSet(BaseViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
