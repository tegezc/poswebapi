from django.urls import path
from .views import RegisterUserView, CreateProductView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
]
