from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CustomUserViewSet,  BicycleViewSet,
                    RentedBicycleViewSet,
                    PriceTypeViewSet)

app_name = "api"
router_v1 = DefaultRouter()


router_v1.register('users', CustomUserViewSet, basename='users')
router_v1.register('bicycles', BicycleViewSet, basename='bicycles')
router_v1.register('price', PriceTypeViewSet, basename='price')
router_v1.register('rentedbicycles', RentedBicycleViewSet,
                   basename='rentedbicycles')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
