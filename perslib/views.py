
from django.shortcuts import render

from .models import User, Login, Logout, Year, Title, Perslib
from .serializers import UserSerializer, LoginSerializer, LogoutSerializer, YearSerializer, TitleSerializer, PerslibSerializer 

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.decorators import action
from rest_framework.response import Response

#Note: ReadOnlyModelViewSet only provide 'read-only' actions:list & .retrieve(). But, ModelViewSet on the otherhand provides the actions: .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().

#Authentication classes:

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.AllowAny]    # Eventhough I set the authentication globally, we need to set the permission class since, by default the permission class is set to AllowAny.

  # A viewset may mark extra actions for routing by decorating a method with the @action decorator. These extra actions will be included in the generated routes. For example, given the set_password method on the UserViewSet class:
  @action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
  def register(self, request):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
  
  

class LoginViewSet(viewsets.ModelViewSet):
  queryset = Login.objects.all()
  serializer_class = LoginSerializer
  permission_classes = [permissions.IsAuthenticated]

class LogoutViewSet(viewsets.ModelViewSet):
  queryset = Logout.objects.all()
  serializer_class = LogoutSerializer
  permission_classes = [permissions.IsAuthenticated]


#Index page (Years):
class YearViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Year.objects.all()
  serializer_class = YearSerializer
  permission_classes = [permissions.AllowAny]   #I let the index page visible without a need for authorization.

#First show page (Titles):
class TitleViewSet(viewsets.ModelViewSet):
  queryset = Title.objects.all()
  serializer_class = TitleSerializer
  permission_classes = [permissions.IsAuthenticated]     #Title page needs authorization

#Second show page (Perlib):
class PerslibViewSet(viewsets.ModelViewSet):              #Perslib page needs authorization
  queryset = Perslib.objects.all()
  serializer_class = PerslibSerializer
  permission_classes = [permissions.IsAuthenticated]

 
