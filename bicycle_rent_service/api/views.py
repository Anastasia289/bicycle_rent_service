from datetime import datetime

from django.shortcuts import get_object_or_404
# from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bicycles.models import Bicycle, RentedBicycle
from users.models import CustomUser

from .serializers import (BicycleSerializer, CustomUserSerializer,
                          RentedBicycleSerializer)


class CustomUserViewSet(UserViewSet):
    """Позволяет просматривать список всех пользователей,
    и свою страницу, а также регистрироваться. Вместе с информацией
    о пользователе получаем его историю аренды велосипедов."""

    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, ]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^email',)
    ordering_fields = ('id', )
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'post', 'patch']

    @action(
        detail=True,
        methods=['patch', ],
        permission_classes=[IsAuthenticated])
    def return_bicycle(self, request, id):
        """Вернуть велосипед."""
        rented_bicycle = RentedBicycle.objects.filter(
            client=request.user, status='rented')
        if not rented_bicycle:
            return Response('У вас нет арендованных велосипедов.',
                            status=status.HTTP_400_BAD_REQUEST)

        bicycle = get_object_or_404(RentedBicycle,
                                    client_id=self.kwargs.get('id'),
                                    status='rented')
        serializer = RentedBicycleSerializer(data={
            'id': bicycle.id,
            'returned_at': datetime.now(),
            'status': 'returned',
            # 'bicycle': bicycle.bicycle.id
            },context={'request': request},partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Велосипед возвращен',
                        status=status.HTTP_204_NO_CONTENT)


class BicycleViewSet(viewsets.ModelViewSet):
    """Вьюсет для велосипедов. Можно просмотреть
    список доступных велосипедов."""

    queryset = Bicycle.objects.filter(status='availible')
    serializer_class = BicycleSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post',]
    pagination_class = None

    @action(
        detail=True,
        methods=['post', ],
        permission_classes=[IsAuthenticated])
    def rent_bicycle(self, request, pk):
        """Арендовать понравившийся велосипед."""
        serializer = RentedBicycleSerializer(
            data={'client': request.user.id, 'bicycle': pk},
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Велосипед арендован',
                        status=status.HTTP_201_CREATED)
