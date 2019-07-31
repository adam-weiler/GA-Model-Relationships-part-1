from django.conf import settings #Needed for foreignkey.
from django.contrib.auth.models import User
from django.db import models
# from django.forms import ModelForm
# from django.utils import timezone # Needed for timezone.localtime()

class Play(models.Model):
    play_name = models.CharField(max_length=255)

    def __str__(self):
        return f"play_name = {self.play_name}"

class Actor(models.Model):
    actor_name = models.CharField(max_length=255)
    play_id = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='actors')

    def __str__(self):
        return f"actor_name = {self.actor_name}"

class Role(models.Model):
    character_name = models.CharField(max_length=255)
    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')

    def __str__(self):
        return f"character name = {self.character_name}"

class Director(models.Model):
    director_name = models.CharField(max_length=255)
    play_id = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='directors')

    def __str__(self):
        return f"director_name = {self.director_name}"