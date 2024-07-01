from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)   #Here I need to register the model for admin by using the UserProfile model I created in models.py.
