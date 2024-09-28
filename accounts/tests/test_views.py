import pytest
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
from accounts.serializers import UserSerializer

@pytest.mark.django_db
class TestUserAPI:
    def test_signup(self, api_client):
        url = reverse('signup')
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone_number": "123456789",
            "birth_date": "2000-01-01",
            "password": "password123"
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == 1
        assert User.objects.get().email == "john@example.com"

    def test_login(self, api_client):
        # Buat user terlebih dahulu
        user = User.objects.create_user(
            name="Jane Doe",
            email="jane@example.com",
            phone_number="987654321",
            birth_date="2000-01-01",
            password="password123"
        )
        
        url = reverse('login')
        data = {
            "email": "jane@example.com",
            "password": "password123"
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data
