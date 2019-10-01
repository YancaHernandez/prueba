from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets,status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from compras.models import Compras
from compras.serializers import comprasSerializer
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
def compras_list(request):
    if request.method == 'GET':
        compras = Compras.objects.all()
        serializer = comprasSerializer(compras, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = comprasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def compras_detail(request, pk):
    try:
        compra = Compras.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({"error":"No existe"},status=400)

    if request.method == 'GET':
        serializer = comprasSerializer(compra)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = comprasSerializer(compra, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        compra.delete()
        return HttpResponse(status=204)