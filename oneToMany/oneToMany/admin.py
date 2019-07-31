from django.contrib import admin
from oneToMany.models import Play, Actor, Role, Director

admin.site.register(Play)
admin.site.register(Actor)
admin.site.register(Role)
admin.site.register(Director)