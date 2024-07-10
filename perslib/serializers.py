# from .models import User
# from .models import Login
from .models import Year
from .models import Title
from .models import Perslib

# from django.contrib.auth.models import User
from rest_framework import serializers
# from django.contrib.auth import get_user_model
# User = get_user_model()

#User Serializers:
#Note: Now, we need to create a serializer object for our API view. A serialize object is an object in the Django rest framework that we can use to describe the data that we need to return and retrieve from our API. TIt converts text string of JSON to a Python object and vice versa.  

# class UserSerializer(serializers.ModelSerializer):
#   class Meta:    # Meta class tells django rest framework what fields we want to take from our model. 
#     model = User
#     fields="__all__"
    # fields = ('id', 'first_name', 'last_name', 'username', 'password', 'profile_picture') 
    #We need the password to be "write only" since we don't need people to see the password in the system.
    # extra_kwargs = {'password': {'write_only': True},'profile_picture': {'read_only': True}}   #Here, kwargs refer to "keyword arguments" and we created a dictionary with curly brackets and we added the key "password" which corresponds to which specific field we want to add special keyword arguments to.
  
  #Below is the special function that overrides the create functionality. This is needed to control how new users are created. The reason for this is we want to be able to assign the password correctly so we want to call the set password function on the model when we assign a password and not just take  the value the user enters as the password. This way, we can encrypt the password as a hash and it won't just store the clear text password in the database.

  # def create(self, validated_data):
  #   #Create and return a new user
  #   user = User(
  #     first_name = validated_data['first_name'],
  #     last_name = validated_data['last_name'],
  #     username = validated_data['username']
  #   )

  #   user.set_password(validated_data['password'])
  #   user.save()

  #   return user


# class LoginSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Login
#     fields = ('id', 'username', 'password') 


#Other Serializers:

class YearSerializer(serializers.ModelSerializer):
  class Meta:
    model = Year
    fields = ('id', 'year',) 

class TitleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Title
    fields = ('id', 'title')  # Here, the type of data is tuple. "Python tuples" store data that should not be modified. Note that the comma is needed if not it would have been a string.


class PerslibSerializer(serializers.HyperlinkedModelSerializer):    #The HyperlinkedModelSerializer class is similar to the ModelSerializer class except that it uses hyperlinks to represent relationships between entities in web API design, rather than primary keys.
  image_url = serializers.ImageField(required=False)
  class Meta:
    model = Perslib
    fields = ['id', 'image_url', 'description', 'date', 'time']


