import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user(User):
    return User.objects.create_user(
        username='TestUser', password='12345678!!!', email='testemail@test.ru'
    )


@pytest.fixture
def user_2(User):
    return User.objects.create_user(
        username='TestUser2', password='12345678!!!2',
        email='testemail2@test.ru'
    )


@pytest.fixture
def another_user(User):
    return User.objects.create_user(
        username='TestUserAnother', password='1234567qwerty',
        email='testemail2@test.ru'
    )


@pytest.fixture
def token(user):
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@pytest.fixture
def user_client(token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
    return client
