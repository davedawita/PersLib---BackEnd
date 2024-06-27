
from django.shortcuts import render

from .models import User
from .models import Year
from .models import Title
from .models import Perslib

from .models import Perslib
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer
from .serializers import YearSerializer
from .serializers import TitleSerializer
from .serializers import PerslibSerializer

from rest_framework.permissions import IsAuthenticated

#Authentication class
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated] 

#Index page class
class YearViewSet(viewsets.ModelViewSet):
  queryset = Year.objects.all()
  serializer_class = YearSerializer
  permission_classes = [permissions.AllowAny]

#First show page
class TitleViewSet(viewsets.ModelViewSet):
  queryset = Title.objects.all()
  serializer_class = TitleSerializer
  permission_classes = [permissions.AllowAny]

#Second show page
class PerslibViewSet(viewsets.ModelViewSet):
  queryset = Perslib.objects.all()
  serializer_class = PerslibSerializer
  permission_classes = [permissions.AllowAny]

 
