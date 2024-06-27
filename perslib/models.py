from django.db import models

class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=32)
  image = models.ImageField(upload_to='images')


class Year(models.Model):
  year = models.PositiveIntegerField()

class Title(models.Model):
  title = models.PositiveIntegerField()

class Perslib(models.Model):
  description = models.CharField(max_length=100)
  date = models.DateField(auto_now=False, auto_now_add=False)
  time = models.TimeField(auto_now=False, auto_now_add=False)   #Note: auto_now is to automatically set the field to now every time the object is saved.Hence, since the app's purpose is not only to include new data but also to include old data, it is set to be false. In addition, auto_now_add is to automatically set the field to now when the object is first created; It is set to be false to enable the user control the entry.
