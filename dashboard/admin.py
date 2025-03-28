

from django.contrib import admin
from .models import Produit, Commande

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'description', 'categorie', 'taille', 'quantite')
    search_fields = ('nom', 'categorie', 'ref')

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('produit', 'quantite', 'date_commande', 'confirme')
    list_filter = ('date_commande', 'confirme')

admin.site.register(Produit, ProduitAdmin)
admin.site.register(Commande, CommandeAdmin)