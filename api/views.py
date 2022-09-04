from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.models import User, Blog
from .serializers import *
from django.contrib import messages
from django.shortcuts import render, redirect
import time



# GET ALL USERS
@api_view([ 'GET' ])
def getUsers(request):
  users = User.objects.all()
  serializer = UserSerializer(users, many = True)
  return Response(serializer.data)


# REGISTER USER

# UPDATE USER

# LOGIN USER

# LOGOUT USER



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
  
  


