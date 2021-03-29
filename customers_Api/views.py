from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomersSerializer
from .models import Customers


@api_view(['GET'])
def showAll(request):
    customers = Customers.objects.all()
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def showOne(request ,id):
    customer = Customers.objects.get(id=id)
    serializer = CustomersSerializer(customer, many=False)
    return Response(serializer.data)