from rest_framework import viewsets

from sensors.models import Manufacturer
from .serializers import ManufacturerSerializer


class ManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
