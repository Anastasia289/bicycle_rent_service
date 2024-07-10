from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import CustomUser

from bicycles.models import (PriceType, Bicycle, RentedBicycle) 

from .serializers import (CustomUserSerializer, PriceTypeSerializer,
                          BicycleSerializer, RentedBicycleSerializer
                          )

# from .filters import BicycleFilter

class CustomUserViewSet(UserViewSet):
    """Позволяет просматривать список всех пользователей,
    и свою страницу, а также регистрироваться."""

    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, ]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('^email',)
    ordering_fields = ('id', )
    serializer_class = CustomUserSerializer
    http_method_names = ['get', 'post']


class BicycleViewSet(viewsets.ModelViewSet):
    """Вьюсет для велосипедов. Можно просмотреть
    список имеющихся велосипедов с указанием того,
    арендованы они уже кем-то или нет."""

    # queryset = Bicycle.objects.filter(status='availible')
    # queryset = Bicycle.objects.filter(is_rented=False)
    queryset = Bicycle.objects.all()
    # filter_backends = (SearchFilter, OrderingFilter)
    filter_backends = (DjangoFilterBackend,)
    # filterset_class = BicycleFilter
    serializer_class = BicycleSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete']
    pagination_class = None

    # @action(
    #     detail=True,
    #     methods=['post', ],
    #     permission_classes=[IsAuthenticated])
    # def rent_bicycle(self, request, pk):
    #     """Арендовать понравившийся велосипед."""
    #     serializer = RentedBicycleSerializer(
    #         data={'client': request.user.id, 'bicycle': pk},
    #         context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     # bicycle = get_object_or_404(Bicycle,
    #     #                             id=self.kwargs.get('pk'))
    #     # bicycle.status='rented'
    #     serializer.save()
       
    #     return Response('Велосипед арендован',
    #                     status=status.HTTP_201_CREATED)

    # @favorite.mapping.delete
    # def favorite_delete(self, request, pk):
    #     """Удалить рецепт из избранного."""
    #     get_object_or_404(Favorite,
    #                       user=self.request.user,
    #                       recipe_id=pk).delete()
    #     return Response('Рецепт удален из избранного',
    #                     status=status.HTTP_204_NO_CONTENT)


class PriceTypeViewSet(viewsets.ModelViewSet):
    """Вьюсет для ингредиентов."""

    queryset = PriceType.objects.all()
    serializer_class = PriceTypeSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class RentedBicycleViewSet(viewsets.ModelViewSet):
    """Вьюсет для ингредиентов."""

    queryset = RentedBicycle.objects.all()
    serializer_class = RentedBicycleSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
