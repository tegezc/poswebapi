# presentation/views.py

from rest_framework.response import Response
from rest_framework.views import APIView
from usecases.register_user import RegisterUser
from usecases.create_product import CreateProduct

class RegisterUserView(APIView):
    def post(self, request, *args, **kwargs):
        use_case = RegisterUser()
        user = use_case.execute(request.data)
        return Response({"user_id": user.id, "message": "User registered successfully!"})

class CreateProductView(APIView):
    def post(self, request, *args, **kwargs):
        use_case = CreateProduct()
        product = use_case.execute(request.data)
        return Response({"product_id": product.id, "message": "Product created successfully!"})
