"""Users serializers."""

# Django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from users.models import User

# Utilities
# import jwt


class UserModelSerializer(serializers.ModelSerializer):

    AUTH_USER_MODEL = "users_management.UserManage" 
    
    """User model serializer."""
    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'email',
        )


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
    )

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Verificar que las contraseñas coicidan."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coiciden")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet :(')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        # token, created = Token.objects.get_or_create(user=self.context['user'])
        # return self.context['user'], token.key
        return data


class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer."""

    token = serializers.CharField()

    def validate_token(self, data):
        # """Verify token is valid."""
        # try:
        #     payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        # except jwt.ExpiredSignatureError:
        #     raise serializers.ValidationError('Verification link has expired.')
        # except jwt.PyJWTError:
        #     raise serializers.ValidationError('Invalid token')
        # if payload['type'] != 'email_confirmation':
        #     raise serializers.ValidationError('Invalid token')

        # self.context['payload'] = payload
        return data

    def save(self):
        """Update user's verified status."""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
