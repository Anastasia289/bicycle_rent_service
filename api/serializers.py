from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
# from api import serializers
from users.models import CustomUser

from bicycles.models import (PriceType, Bicycle, RentedBicycle) 

MIN_PASSWORD_LENGTH = 5


class CustomUserSerializer(UserSerializer):
    """Сериализатор для управления пользователями."""

    # is_subscribed = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email',)

    # def get_rented_bicycles(self, obj):
    #     return RentedBicycle.objects.filter(
    #        ).


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', )


class PriceTypeSerializer(serializers.ModelSerializer):
    """Сериализатор для избранного."""

    class Meta:
        model = PriceType
        fields = ('id', 'name', 'price', )


class BicycleSerializer(serializers.ModelSerializer):
    """Сериализатор для избранного."""
    is_rented = SerializerMethodField()

    class Meta:
        model = Bicycle
        fields = ('id', 'name', 'description', 'rental_cost',
                  'status', 'is_rented')

    def get_is_rented(self, obj):
        return RentedBicycle.objects.filter(
            bicycle=obj, status='rented').exists()


class RentedBicycleSerializer(serializers.ModelSerializer):
    """Сериализатор для аренды велосипеда."""

    class Meta:
        model = RentedBicycle
        fields = ('id', 'client', 'bicycle', 'rented_at',
                  'status', 'returned_at')

    def validate(self, data):
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
        return data

    def bicycle_status_rented(self, id):
        bicycle = Bicycle.objects.get(name=id)
        bicycle.status = 'rented'

    def create(self, validated_data):
        # bicycle = self.context.get('bicycle')
        # self.bicycle_status_rented(bicycle)
        # validated_data['bicycle'].status='rented'
        rented_bicycle = RentedBicycle.objects.create(**validated_data)
        # validated_data['bicycle'].status = 'rented'

        return rented_bicycle

    # def update(self, recipe, validated_data):

    #     recipe.tags.set(self.initial_data.get('tags'))
    #     RecipyIngredients.objects.filter(recipes=recipe).all().delete()
    #     ingredients = validated_data.pop('recipy_ingredient')
    #     self.create_recipy_ingredients(ingredients, recipe)
    #     return super().update(recipe, validated_data)
