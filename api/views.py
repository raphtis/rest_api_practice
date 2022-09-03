from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.models import User, Blog
from .serializers import *


# GET ALL ITEMS IN DB
@api_view([ 'GET' ])
def getData(request):
  items = Item.objects.all()
  serializer = ItemSerializer(items, many = True)
  return Response(serializer.data)


# CREATE ITEM
@api_view([ 'POST' ])
def createTicket(request):
  serializer = ItemSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status = status.HTTP_201_CREATED)

# GET SINGLE ITEM IN DB
@api_view([ 'GET', 'PUT', 'DELETE' ])
def itemDetail(request, id):
  
  try:
    item = Item.objects.get(pk=id)
  except Item.DoesNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = ItemSerializer(item)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    item.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)
  
  


