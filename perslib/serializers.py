from .models import Perslib
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class PerslibSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Perslib
    fields = ['id', 'description', 'date', 'time']