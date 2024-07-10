from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser    #This is the base user in django.
from django.db.models.signals import post_save
from django.contrib.auth.models import PermissionsMixin     #This allows us to set what users can and cannot do.
from django.contrib.auth.models import UserManager

#User Models:

class UserProfile(AbstractBaseUser, PermissionsMixin):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=255)  
  username = models.CharField(max_length=30, unique=True)
  password = models.CharField(max_length=100)
  profile_picture = models.ImageField(upload_to='profile_picture', blank=True, null=True)  

  is_staff = models.BooleanField(default=False)    #This is done because we don't need new users to come in as staff members.
  
  objects = UserManager() #We can use this to help the superuser by managing other managers to handle accounts of users.

  REQUIRED_FIELDS = ['first_name', 'last_name']
  USERNAME_FIELD = 'username'


class User(models.Model):
  
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=255, blank=True, null=True)
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=32)
  re_password = models.CharField(max_length=32,null=True)
  profile_picture = models.ImageField(upload_to='profile_picture', blank=True, null=True)
  
  is_staff = models.BooleanField(default=False) #This is done because we don't need new users to come in as staff members.
  is_superuser = models.BooleanField(default=False) 
 

  REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'password']

    
def create_profile(sender, **kwargs):
  if kwargs['created']:
    user_profile = UserProfile.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile, sender=User)

  if not is_superuser:
    disabled_fields |= {
        'username',
        'is_superuser',
        'user_permissions',
    }
  
  # Prevent non-superusers from editing their own permissions
  if (
      not is_superuser
      and obj is not None
      and obj == request.user
  ):
      disabled_fields |= {
          'is_staff',
          'is_superuser',
          'groups',
          'user_permissions',
      }
    
class Login(models.Model):  
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=32) 

#Other Models:

class Year(models.Model):
  year = models.PositiveIntegerField()

class Title(models.Model):
  title = models.CharField(max_length=20)   

class Perslib(models.Model):
  image_url = models.ImageField(upload_to='post_images', blank=True, null=True)
  description = models.CharField(max_length=100)
  date = models.DateField(auto_now=False, auto_now_add=False)
  time = models.TimeField(auto_now=False, auto_now_add=False)   #Note: auto_now is to automatically set the field to now every time the object is saved.Hence, since the app's purpose is not only to include new data but also to include old data, it is set to be false. In addition, auto_now_add is to automatically set the field to now when the object is first created; It is set to be false to enable the user control the entry.
