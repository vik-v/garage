from rest_framework import viewsets

from sensors.models import Sensor
from .serializers import SensorSerializer


class SensorsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
