from .models import User
from .models import Login
from .models import Logout
from .models import Year
from .models import Title
from .models import Perslib

from django.contrib.auth.models import User, Group
from rest_framework import serializers

#User Serializers:

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'username', 'password') 

class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = Login
    fields = ('id', 'username', 'password') 

class LogoutSerializer(serializers.ModelSerializer):
  class Meta:
    model = Logout
    fields = ('id', 'username', 'password') 


#Other Serializers:

class YearSerializer(serializers.ModelSerializer):
  class Meta:
    model = Year
    fields = ('year') 

class TitleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Title
    fields = ('title') 


class PerslibSerializer(serializers.HyperlinkedModelSerializer):    #The HyperlinkedModelSerializer class is similar to the ModelSerializer class except that it uses hyperlinks to represent relationships between entities in web API design, rather than primary keys.
  class Meta:
    model = Perslib
    fields = ['id', 'description', 'date', 'time']


