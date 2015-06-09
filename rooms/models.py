from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)


class Room(models.Model):
    building = models.ForeignKey(Building)
    room_number = models.CharField(max_length=256)
    room_type = models.CharField(max_length=256)
    manager = models.CharField(max_length=256)
    general_usage = models.BooleanField()
    seating = models.IntegerField()
    display = models.BooleanField()
    phone = models.BooleanField()
    network = models.BooleanField()
    usage_restrictions = models.CharField(max_length=256)
    has_usage_restrictions = models.BooleanField()
