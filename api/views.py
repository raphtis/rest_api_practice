from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.http import JsonResponse
from base.models import *
from knox.models import AuthToken
from knox.auth import AuthToken, TokenAuthentication
from .serializers import *
from django.contrib import messages

import time


def serialize_user(user):
  return {
    "username": user.username,
    "email": user.email,
    "first_name": user.first_name,
    "last_name": user.last_name,
  }


# REGISTER USER
@api_view([ 'POST' ])
def register(request):
  serializer = RegisterSerializer(data = request.data)
  serializer.is_valid(raise_exception=True)
  
  user = serializer.save()
  _, token = AuthToken.objects.create(user)
  
  return Response({
    'user_info': serialize_user(user),
    'token': token
  })

# LOGIN USER
@api_view([ 'POST' ])
def login(request):
  serializer = AuthTokenSerializer(data=request.data)
  serializer.is_valid(raise_exception=True)
  user = serializer.validated_data['user']
  _, token = AuthToken.objects.create(user)
  
  return Response({
    'user_info': serialize_user(user),
    'token': token
  })


# GET USER
@api_view([ 'GET' ])
def user_info(request):
  user = request.user
  if user.is_authenticated:
    return Response({
      'user_data': serialize_user(user),
    })
  return Response({})


# UPDATE USER



# LOGOUT USER
# HANDLED BY KNOX



# GET ALL ITEMS IN DB
@api_view([ 'GET' ])
def getData(request):
  blogs = Blog.objects.all()
  serializer = BlogSerializer(blogs, many = True)
  return Response(serializer.data)


# CREATE ITEM
@api_view([ 'POST' ])
def createTicket(request):
  serializer = BlogSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status = status.HTTP_201_CREATED)


# GET SINGLE ITEM IN DB
@api_view([ 'GET', 'PUT', 'DELETE' ])
def blogDetail(request, id):
  
  try:
    blog = Blog.objects.get(pk=id)
  except Blog.DoesNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = BlogSerializer(blog)
    return Response(serializer.data)
  
  elif request.method == 'PUT':
    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    blog.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)
  
  


