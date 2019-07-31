from django.conf import settings #Needed for foreignkey.
from django.contrib.auth.models import User
from django.db import models
# from django.forms import ModelForm
from django.utils import timezone # Needed for timezone.localtime()

#Question 1 - Plays:
class Play(models.Model): #Play must be written first.
    play_name = models.CharField(max_length=255)

    def __str__(self):
        return f"play_name = {self.play_name}"

class Actor(models.Model):
    actor_name = models.CharField(max_length=255)
    play_id = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='actors')

    def __str__(self):
        return f"actor_name = {self.actor_name}"

class Director(models.Model):
    director_name = models.CharField(max_length=255)
    play_id = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='directors')

    def __str__(self):
        return f"director_name = {self.director_name}"

class Role(models.Model):
    character_name = models.CharField(max_length=255)
    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')

    def __str__(self):
        return f"character name = {self.character_name}"



# Question 2 - Vet clinic:

class Breed(models.Model): #Breed must be written first.
    breed_name = models.CharField(max_length=255)

    def __str__(self):
        return f"breed_name = {self.breed_name}"

class Clinic(models.Model): #Clinic must be written first.
    clinic_name = models.CharField(max_length=255)
    clinic_address = models.CharField(max_length=255)

    def __str__(self):
        return f"clinic_name = {self.clinic_name}"

class Owner(models.Model): #Owner must be written first.
    owner_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"owner_name = {self.owner_name}"

class Veterinarian(models.Model): #Veterinarian must be written second.
    veterinarian_name = models.CharField(max_length=255)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='clinics')

    def __str__(self):
        return f"veterinarian_name = {self.veterinarian_name}"

class Pet(models.Model): #Pet must be written second.
    pet_name = models.CharField(max_length=255)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owners')
    breed_id = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='breeds')

    def __str__(self):
        return f"pet_name = {self.pet_name}"

class Appointment(models.Model):
    appointment_date = models.DateTimeField(default=timezone.localtime())
    veterinarian_id = models.ForeignKey(Veterinarian, on_delete=models.CASCADE, related_name='veterinarians')
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return f"appointment_date = {self.appointment_date}"

