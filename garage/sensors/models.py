from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

User = get_user_model()


class ModelWithDescription(models.Model):
    description = models.TextField('Description',
                                   blank=True,
                                   null=True,)

    class Meta:
        abstract = True


class Garage(ModelWithDescription):
    name = models.CharField('Garage name',
                            max_length=255,
                            blank=True,
                            null=True)
    number = models.IntegerField(unique=True)

    class Meta:
        verbose_name = 'Garage'
        verbose_name_plural = 'Garages'

    def __str__(self) -> str:
        return 'Garage N: ' + str(self.number)


class Room(ModelWithDescription):
    FLOOR_VALUES = [
        ('B', 'Basement'),
        ('F', 'First floor'),
        ('S', 'Second floor')
    ]
    name = models.CharField('Room name',
                            max_length=255)
    floor = models.CharField('Floor',
                             max_length=1,
                             choices=FLOOR_VALUES)
    garage = models.ForeignKey(Garage,
                               on_delete=models.CASCADE,
                               related_name="garage",
                               related_query_name="garage",)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self) -> str:
        return ('Room: ' + self.name + ' is suited on '
                + self.get_floor_display().lower()
                + ' at garage ' + str(self.garage.number))


class Manufacturer(ModelWithDescription):
    name = models.CharField('Manufacturer name',
                            unique=True,
                            max_length=255)
    country = CountryField('Country')
    url = models.URLField(blank=True,
                          null=True,)

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'


class Sensor(ModelWithDescription):
    SENSOR_TYPES = (
        ('DHT', 'Temperature and humidity'),
        ('PIR', 'Motin detection'),
        ('PR', 'Pressure sensor'),
    )

    name = models.CharField('Sensor name',
                            max_length=255)
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.SET_NULL,
                                     blank=True,
                                     null=True)
    type = models.CharField('Sensor type',
                            max_length=3,
                            choices=SENSOR_TYPES)
    room = models.ForeignKey(Room,
                             on_delete=models.CASCADE,
                             related_name="room",
                             related_query_name="room",)
    status = models.BooleanField('Status')

    class Meta:
        pass


class DHT(Sensor):
    temperature = models.FloatField('Temperature',
                                    blank=True,
                                    null=True)
    humidity = models.FloatField('Humidity',
                                 blank=True,
                                 null=True)


class PIR(Sensor):
    detection = models.BooleanField('Motion detection')


class PR(Sensor):
    pressure = models.FloatField('Pressure')


class Statistic(models.Model):
    action_date_start = models.DateTimeField()
    action_date_end = models.DateTimeField()
    sensor = models.ForeignKey(Sensor,
                               on_delete=models.CASCADE,
                               related_name="sensor",
                               related_query_name="sensor",)

    class Meta:
        pass
