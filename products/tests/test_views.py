import pytest
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
from accounts.serializers import UserSerializer
from products.models import Product
from products.serializers import ProductSerializer

@pytest.mark.django_db
class TestProductAPI:
    def test_create_product(self, api_client):
        # Buat user dan login untuk mendapatkan token
        user = User.objects.create_user(
            name="Admin User",
            email="admin@example.com",
            phone_number="123123123",
            birth_date="2000-01-01",
            password="password123"
        )
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Set header authorization
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        # Buat produk
        url = reverse('product')
        data = {
            "name": "Produk A",
            "nip": "NIP123456",
            "stock": 10
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Product.objects.count() == 1
        assert Product.objects.get().name == "Produk A"

    def test_get_all_products(self, api_client):
        # Buat user dan login untuk mendapatkan token
        user = User.objects.create_user(
            name="Admin User",
            email="admin@example.com",
            phone_number="123123123",
            birth_date="2000-01-01",
            password="password123"
        )
        
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        # Set header authorization
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        # Buat produk
        Product.objects.create(name="Produk A", nip="NIP123456", stock=10)
        Product.objects.create(name="Produk B", nip="NIP654321", stock=5)

        url = reverse('product')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2  # Pastikan jumlah produk yang dikembalikan benar
