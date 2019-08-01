from django.contrib import admin
from manyToMany.models import Film, Viewer, Films_Watched

admin.site.register(Film) #Play must be called first.
admin.site.register(Viewer)
admin.site.register(Films_Watched)