from categorias.models import Categorias
from rest_framework import serializers


class categoriasSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    nombre=serializers.CharField()

    def create(self,validated_data):
        instance=Categorias()
        instance.nombre=validated_data.get('nombre')
        return instance

    def update(self, instance, validated_data):
        instance.nombre=validated_data.get('nombre',instance.nombre)
        instance.save()

