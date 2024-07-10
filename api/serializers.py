from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
# from rest_framework.fields import SerializerMethodField

from users.models import CustomUser

MIN_PASSWORD_LENGTH = 5


class CustomUserSerializer(UserSerializer):
    """Сериализатор для управления пользователями."""

    # is_subscribed = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'username', 'password', )

    # def get_is_subscribed(self, obj):
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         return Subscriptions.objects.filter(user=user,
    #                                             author=obj).exists()
    #     return False


class CustomUserCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email',)
