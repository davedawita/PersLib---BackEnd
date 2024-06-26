from django.shortcuts import render
from .models import Perslib
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PerslibSerializer

class PerslibViewSet(viewsets.ModelViewSet):
  queryset = Perslib.objects.all()
  serializer_class = PerslibSerializer
  permission_classes = [permissions.AllowAny]
