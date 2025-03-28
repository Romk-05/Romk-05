# comptes/admin.py

from django.contrib import admin
from .models import Profil

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenoms', 'sexe', 'role')
    search_fields = ('nom', 'prenoms', 'role')

admin.site.register(Profil, ProfilAdmin)