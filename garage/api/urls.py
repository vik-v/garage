from api.views import (
    ManufacturerViewSet,
)

from django.urls import include, path

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter


app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('manufacturers',
                   ManufacturerViewSet,
                   basename='manufacturers')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
