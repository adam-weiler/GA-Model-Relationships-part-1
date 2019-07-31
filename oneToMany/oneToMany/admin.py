from django.contrib import admin
from oneToMany.models import Play, Actor, Director, Role
from oneToMany.models import Breed, Clinic, Owner, Veterinarian, Pet, Appointment
from oneToMany.models import Publication, Restaurant, Chef, Critic, Review

admin.site.register(Play) #Play must be called first.
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Role)

admin.site.register(Breed) #Breed must be written first.
admin.site.register(Clinic) #Clinic must be written first.
admin.site.register(Owner) #Owner must be written first.
admin.site.register(Veterinarian) #Veterinarian must be written second.
admin.site.register(Pet) #Pet must be written second.
admin.site.register(Appointment)

admin.site.register(Publication) #Publication must be written first.
admin.site.register(Restaurant) #Restaurant must be written first.
admin.site.register(Chef)
admin.site.register(Critic)
admin.site.register(Review)