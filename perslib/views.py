from .models import User, Login, Year, Title, Perslib
from .serializers import UserSerializer, LoginSerializer, YearSerializer, TitleSerializer, PerslibSerializer

from rest_framework import viewsets
from rest_framework import filters

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.settings import api_settings
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

#Note: ReadOnlyModelViewSet only provide 'read-only' actions:list & .retrieve(). But, ModelViewSet on the otherhand provides the actions: .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().

#Authentication classes:

class UserViewSet(viewsets.ModelViewSet):
  #Handles reading, creating and updating user profiles
  serializer_class = UserSerializer
  permission_classes = [permissions.AllowAny]
  queryset = User.objects.all()     #This queryset tells the viewset how to retrieve the object from the database 
  

class LoginViewSet(viewsets.ViewSet):
  #This checks username and password and returns an auth token.
  serializer_class = AuthTokenSerializer
  permission_classes = [permissions.AllowAny]
  def create(self, request):
    #Use the ObtainAuthToken APIView to validate and create a token.
    #Handle creating user authentication tokens
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    return ObtainAuthToken().as_view()(request=request._request) 
  

class Logout(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request,format=None):
    #To delete the token to force a login:
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

#Index page (Years):
# Eventhough I set the authentication globally, I need to set the permission class since, by default the permission class is set to AllowAny.

class YearViewSet(viewsets.ModelViewSet):
  #Note: If ReadOnlyModelViewSet used in place of ModelViewSet, it does not allow editing! If checked by postman,POST & PUT will not succeed to create or change anything.
  queryset = Year.objects.all()
  serializer_class = YearSerializer
  permission_classes = [permissions.AllowAny]   #I let the index page visible without a need for authorization.


#First show page (Titles):
class TitleViewSet(viewsets.ModelViewSet):   
  queryset = Title.objects.all()
  serializer_class = TitleSerializer
  permission_classes = [permissions.IsAuthenticated]     #Title page needs authorization

#Second show page (Perlib):
class PerslibViewSet(viewsets.ModelViewSet):              
  queryset = Perslib.objects.all()
  serializer_class = PerslibSerializer
  permission_classes = [permissions.IsAuthenticated]      #Perslib page needs authorization

 
