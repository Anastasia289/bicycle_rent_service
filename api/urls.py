from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CustomUserViewSet)

app_name = "api"
router_v1 = DefaultRouter()

# router_v1.register('main', MainViewSet, basename='main')
router_v1.register('users', CustomUserViewSet, basename='employee')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
