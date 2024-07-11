import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

import tests.conftest as conftest

User = get_user_model()


@pytest.mark.django_db
class TestUsersUrls:
    def test_user_registration(self, client):
        url = reverse("users:user-registration")
        data = {
            "username": conftest.TEST_USERNAME,
            "password": conftest.TEST_PASSWORD,
            "email": conftest.TEST_EMAIL,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED