# comptes/models.py

from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=150)
    sexe = models.CharField(max_length=1)  # 'M' pour masculin, 'F' pour féminin
    role = models.CharField(max_length=50)  # Vendeur ou Administrateur

    def __str__(self):
        return f"{self.nom} {self.prenoms} - {self.role}"
    