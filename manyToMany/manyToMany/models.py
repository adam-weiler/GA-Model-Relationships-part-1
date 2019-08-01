from django.conf import settings #Needed for foreignkey.
from django.contrib.auth.models import User
from django.db import models
# from django.forms import ModelForm
from django.utils import timezone # Needed for timezone.localtime()


# 1. Imagine an app that allows users to keep track of what films they've seen:

class Film(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f'title = {self.title}'

class Viewer(models.Model):
    user_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f'user_name = {self.user_name}'

class Films_Watched(models.Model):
    appointment_date = models.DateTimeField(default=timezone.localtime())
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='films')
    viewer_id = models.ForeignKey(Viewer, on_delete=models.CASCADE, related_name='viewers')
    
    def __str__(self):
        return f'film_id = {self.film_id}, viewer_id = {self.viewer_id}'





