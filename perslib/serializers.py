from .models import User
from .models import Year
from .models import Title
from .models import Perslib

from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'username', 'password', 'image') 

class YearSerializer(serializers.ModelSerializer):
  class Meta:
    model = Year
    fields = ('year') 

class TitleSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('title') 


class PerslibSerializer(serializers.HyperlinkedModelSerializer):    #The HyperlinkedModelSerializer class is similar to the ModelSerializer class except that it uses hyperlinks to represent relationships between entities in web API design, rather than primary keys.
  class Meta:
    model = Perslib
    fields = ['id', 'description', 'date', 'time']


