from productos.models import Productos
from categorias.models import Categorias
from tiendas.models import Tiendas
from rest_framework import serializers


class productosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Productos
        fields = ["id",'nombre', 'precio', 'categoria',"tienda"]
        

    def create(self,validated_data):
        producto = Productos.objects.create(**validated_data)
        return producto

    def update(self, instance, validated_data):
        instance.nombre=validated_data.get('nombre',instance.nombre)
        instance.precio=validated_data.get('precio',instance.precio)
        instance.categoria=validated_data.get('categoria',instance.categoria)
        instance.tienda=validated_data.get('tienda',instance.tienda)
        instance.save()
        return instance

