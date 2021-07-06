from ..models import User
from rest_framework import serializers
from django.contrib.auth import password_validation


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'street', 'zip_code', 'city']


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'passowrd': {'write_only': True}
        }

    def validate(self, data):
        password = data.get('password')
        password2 = data.pop('password2')
        email = data['email']

        if password != password2:
            raise serializers.ValidationError('Passwords are diffrent')

        password_validation.validate_password(password, self.instance)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('This email is already exist')

        return data

    def create(self, data):
        password = data.get('password')
        email = data['email']

        user = User(
            username=email,
            email=email)

        user.set_password(password)
        user.save()

        return user
