from django.urls import path
from .views import RegisterUserView, CreateProductView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
]

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateUserView, LoginView

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
