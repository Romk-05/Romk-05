
from django.conf import settings
from django.conf.urls.static import static
from .views import vendeur_view, parametre_view

from django.urls import path
from .views import admin_dashboard, vendeur_dashboard, commande_view, produit_view, deconnexion_view, confirmer_commande



urlpatterns = [
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('vendeur/', vendeur_dashboard, name='vendeur_dashboard'),
    path('vendeurs/', vendeur_view, name='vendeurs'),  # New URL for rendering vendeur.html
    path('commandes/', commande_view, name='commandes'),
    path('produits/', produit_view, name='produits'),
    path('parametre/', parametre_view, name='paramtre'),
    path('deconnexion/', deconnexion_view, name='deconnexion'),
    path('confirmer_commande/<int:commande_id>/', confirmer_commande, name='confirmer_commande'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
