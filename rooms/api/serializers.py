from rooms import models
from rest_framework import serializers


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Building


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
