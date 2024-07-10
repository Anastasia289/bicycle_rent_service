# from django.shortcuts import get_object_or_404
# from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import status  # viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser

from .serializers import (CustomUserSerializer,
                          )


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

    @action(
        detail=False,
        methods=['get'],
        url_path='me',
        permission_classes=[IsAuthenticated,])
    def profile(self, request):
        """Просмотр информации о себе."""
        serializer = CustomUserSerializer(
            self.request.user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
