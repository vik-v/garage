from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Garage(models.Model):
    name = models.CharField()
    description = models.CharField()
    number = models.IntegerField()

    class Meta:
        pass


class Room(models.Model):
    name = models.CharField()
    description = models.CharField()
    floor = models.SmallIntegerField()
    garage = models.ForeignKey(Garage,
                               on_delete=models.CASCADE,
                               related_name="garage",
                               related_query_name="garage",)

    class Meta:
        pass


class Manufacturer(models.Model):
    name = models.CharField()
    description = models.CharField(blank=True,)
    url = models.URLField()

    class Meta:
        pass


class SensorType(models.Model):
    type = models.CharField()
    description = models.CharField(blank=True,)

    class Meta:
        pass


class Sensor(models.Model):
    name = models.CharField('Sensor name')
    description = models.CharField('Sensor description',
                                   blank=True,)
    manufacturer = models.ForeignKey(Manufacturer,
                                     blank=True,)
    type = models.ForeignKey(SensorType,
                             on_delete=models.CASCADE,
                             related_name="sensor_type",
                             related_query_name="sensor_type",)
    room = models.ForeignKey(Room,
                             on_delete=models.CASCADE,
                             related_name="rooms",
                             related_query_name="room",)
    status = models.BooleanField()

    class Meta:
        pass
