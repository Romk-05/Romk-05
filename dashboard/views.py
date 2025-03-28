

from django.shortcuts import render, redirect, get_object_or_404
from .models import Commande, Produit

def admin_dashboard(request):
    commandes = Commande.objects.filter(confirme=True)  # Commandes confirmées
    return render(request, 'dashboard/admin/index.html', {'commandes': commandes})

def vendeur_dashboard(request):
    return render(request, 'dashboard/vendeur/commandeV.html')

def commande_view(request):
    commandes = Commande.objects.filter(confirme=False)  # Commandes non confirmées
    total_amount = sum(commande.quantite * commande.produit.prix for commande in commandes) if commandes else 0
    return render(request, 'dashboard/vendeur/commandeV.html', {
        'commandes': commandes,
        'total_amount': total_amount,
    })

def produit_view(request):
    if request.method == "POST":
        # Obtain the data from the form to create a new product
        nom = request.POST['nom']
        description = request.POST['description']
        prix = request.POST['prix']
        image = request.FILES['image']
        categorie = request.POST['categorie']
        taille = request.POST['taille']
        ref = request.POST['ref']
        quantite = request.POST['quantite']

        # Create and save the product
        produit = Produit(
            nom=nom,
            description=description,
            prix=prix,
            image=image,
            categorie=categorie,
            taille=taille,
            ref=ref,
            quantite=quantite
        )
        produit.save()
        
        return redirect('produits')  # Redirect to the page that lists products

    return render(request, 'dashboard/vendeur/produitV.html')

def confirmer_commande(request, commande_id):
    commande = get_object_or_404(Commande, pk=commande_id)
    commande.confirme = True
    commande.save()
    return redirect('admin_dashboard')  # Redirecting to admin dashboard

def deconnexion_view(request):
    request.session.flush()  # Clear session
    return redirect('connexion')  # Redirect to login page

# dashboard/views.py

def vendeur_view(request):
    produits = Produit.objects.all()  
    return render(request, 'dashboard/admin/vendeur.html', {'produits': produits})

def parametre_view(request):
    return render(request, 'dashboard/admin/paramtre.html')   