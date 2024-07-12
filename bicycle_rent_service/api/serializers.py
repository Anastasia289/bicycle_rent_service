# import datetime
import math

from bicycles.models import Bicycle, RentedBicycle
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from users.models import CustomUser

from bicycle_rent_service.constants import SEC_IN_HOUR


class CustomUserSerializer(UserSerializer):
    """Сериализатор для управления пользователями."""

    rented_bicycles = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'rented_bicycles',)

    def get_rented_bicycles(self, obj):
        rented_bicycles = RentedBicycle.objects.filter(client_id=obj).all()
        return RentedBicycleSerializer(rented_bicycles, many=True).data


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', )


class BicycleSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра велосипедов."""

    class Meta:
        model = Bicycle
        fields = ('id', 'name', 'description', 'rental_cost',
                  'status',)


class RentedBicycleSerializer(serializers.ModelSerializer):
    """Сериализатор для аренды велосипеда."""

    rented_time_in_hours = SerializerMethodField()
    price_per_hour = SerializerMethodField()
    final_price = SerializerMethodField()

    class Meta:
        model = RentedBicycle
        fields = ('id', 'client', 'bicycle', 'rented_at',
                  'status', 'returned_at', 'final_price',
                  'price_per_hour', 'rented_time_in_hours')

    # def validate(self, data):
        
    #     if data['bicycle'].status != 'availible':
    #         raise serializers.ValidationError(
    #             'Этот велосипед арендовать нельзя, выберите другой')
    #     if RentedBicycle.objects.filter(
    #         client=self.context.get(
    #             'request').user, status='rented').exists():
    #         raise serializers.ValidationError(
    #             'Вы не можете арендовать несколько велосипедов одновременно')
    #     if RentedBicycle.objects.filter(
    #         client=self.context.get(
    #             'request').user, status='damaged').exists():
    #         raise serializers.ValidationError(
    #             'Ужасный вы человек. '
    #             'Велосипеды вас боятся и арендоваться не хотят :) '
    #             'Для примирения обратитесь к администратору. ')
    #     return data

    def validate(self, data):
        if not 'id':
            if data['bicycle'].status != 'availible':
                raise serializers.ValidationError(
                    'Этот велосипед арендовать нельзя, выберите другой')
            if RentedBicycle.objects.filter(
                client=self.context.get(
                    'request').user, status='rented').exists():
                raise serializers.ValidationError(
                    'Вы не можете арендовать несколько велосипедов одновременно')
            if RentedBicycle.objects.filter(
                client=self.context.get(
                    'request').user, status='damaged').exists():
                raise serializers.ValidationError(
                    'Ужасный вы человек. '
                    'Велосипеды вас боятся и арендоваться не хотят :) '
                    'Для примирения обратитесь к администратору. ')
        if 'returned_at':
            if 'returned_at' <= 'rented_at':
                raise serializers.ValidationError(
                    'Проверьте время аренды')
        return data

    def bicycle_status_rented(self, b):
        """Меняем статус велосипеда на 'арендован'."""
        Bicycle.objects.filter(id=b).update(status='rented')

    def bicycle_status_availible(self, b):
        """Меняем статус велосипеда на 'доступен'."""
        Bicycle.objects.filter(id=b).update(status='availible')

    def get_rented_time_in_hours(self, obj):
        """Расчет количества часов, на которые был арендован
        велосипед. Аренда почасовая. """
        if obj.returned_at:
            timedelta = obj.returned_at - obj.rented_at
            return math.ceil(timedelta.total_seconds() / SEC_IN_HOUR)

    def get_price_per_hour(self, obj):
        """Показать стоимость в час"""
        price = obj.bicycle.rental_cost.price
        return price

    def get_final_price(self, obj):
        """Расчет стоимости аренды на основе времени."""
        price = self.get_price_per_hour(obj)
        hours = self.get_rented_time_in_hours(obj)
        if hours:
            return price * hours

    def create(self, validated_data):
        bicycle = self.initial_data.get('bicycle')
        self.bicycle_status_rented(bicycle)
        rented_bicycle = RentedBicycle.objects.create(**validated_data)
        return rented_bicycle

    def update(self, rented_bicycle, validated_data):
        bicycle = self.initial_data.get('bicycle')
        self.bicycle_status_availible(bicycle)
        return super().update(rented_bicycle, validated_data)
