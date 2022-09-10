from rest_framework import serializers, validators
from django.contrib.auth.models import User
from base.models import *

class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
  class Meta: 
    model = User
    fields = ('username', 'password', 'email', 'first_name', 'last_name')
  
    extra_kwargs = {
      "password": {"write_only": True},
      "email":{
        "required": True,
        "allow_blank": False,
        "validators": [
          validators.UniqueValidator(
            User.objects.all(), "A user with that email already exists."
          )
        ]
      }
    }
    
  def create(self, validated_data):
    user = User(
      email=validated_data.get('email'),
      username=validated_data.get('username'),
      first_name=validated_data.get('first_name'),
      last_name=validated_data.get('last_name'),
    )
    user.set_password(validated_data.get('password'))
    user.save()
    return user
    