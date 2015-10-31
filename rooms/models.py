from django.db import models
from django.utils.text import slugify


class Building(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    slug = models.SlugField()

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        return super(Building, self).save(*args, **kwargs)


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
    slug = models.SlugField()

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify('%s %s' % (self.room_type, self.room_number))

        return super(Room, self).save(*args, **kwargs)
