# usecases/register_user.py

from domain.models import User
from django.contrib.auth.hashers import make_password

class RegisterUser:
    def execute(self, data):
        user = User(
            nama=data.get('nama'),
            email=data.get('email'),
            nomor_telp=data.get('nomor_telp'),
            tanggal_lahir=data.get('tanggal_lahir'),
            password=make_password(data.get('password'))
        )
        user.save()
        return user
