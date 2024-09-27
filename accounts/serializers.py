from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'phone_number', 'birth_date', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        # Membuat instance user baru
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            birth_date=validated_data['birth_date']
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()  # Simpan user ke database
        return user  # Kembalikan instance user yan