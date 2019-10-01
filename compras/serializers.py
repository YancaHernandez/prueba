from compras.models import Compras
from rest_framework import serializers

from productos.models import Productos

from django.conf import settings

# import jwt

class comprasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compras
        fields = (
            "id",'cantidad','producto','user'
        )

    def create(self,validated_data):
        compra = Compras.objects.create(**validated_data)
        return compra

    def update(self, instance, validated_data):
        instance.cantidad=validated_data.get('cantidad',instance.cantidad)
        instance.producto=validated_data.get('producto',instance.producto)
        instance.save()
        return instance

    # def validate(self, data):
    #     try:
    #         payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
    #     except jwt.ExpiredSignatureError:
    #         raise serializers.ValidationError('Verification link has expired.')
    #     except jwt.PyJWTError:
    #         raise serializers.ValidationError('Invalid token')
    #     if payload['type'] != 'email_confirmation':
    #         raise serializers.ValidationError('Invalid token')
       




