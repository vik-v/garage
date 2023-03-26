from django.contrib import admin
from .models import (
    DHT,
    Garage,
    Manufacturer,
    Room,
    Statistic,
)

admin.site.register(Garage)
admin.site.register(Room)
admin.site.register(Manufacturer)
admin.site.register(DHT)
admin.site.register(Statistic)
