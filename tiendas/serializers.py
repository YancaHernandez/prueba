from tiendas.models import Tiendas
from rest_framework import serializers


class tiendasSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    nombre=serializers.CharField()

    def create(self,validated_data):
        instance=Tiendas()
        instance.nombre=validated_data.get('nombre')
        return instance

    def update(self, instance, validated_data):
        instance.nombre=validated_data.get('nombre',instance.nombre)
        instance.save()

