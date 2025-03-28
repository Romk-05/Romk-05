# dashboard/models.py

from django.db import models

class Produit(models.Model):
    CATEGORIES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Enfant', 'Enfant'),
    ]

    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits/images/')
    categorie = models.CharField(
        max_length=10,
        choices=CATEGORIES,
        default='Homme'
    )
    taille = models.CharField(max_length=10)
    ref = models.CharField(max_length=50)
    quantite = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)  # Link to the Produit model
    quantite = models.PositiveIntegerField()  # Quantity ordered
    date_commande = models.DateTimeField(auto_now_add=True)  # Date when the order was placed
    confirme = models.BooleanField(default=False)  # Status of the order

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom} - Confirmée: {self.confirme}"