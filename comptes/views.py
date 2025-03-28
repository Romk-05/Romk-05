# # comptes/views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from .models import Profil

# def inscription_view(request):
#     if request.method == "POST":
#         nom = request.POST.get('nom')
#         prenoms = request.POST.get('prenoms')
#         sexe = request.POST.get('sexe')
#         role = request.POST.get('role')
#         login_user = request.POST.get('login')
#         password = request.POST.get('password')

#         # Créer un nouvel utilisateur
#         user = User.objects.create_user(username=login_user, password=password)
#         # Créer un profil associé à cet utilisateur
#         Profil.objects.create(user=user, nom=nom, prenoms=prenoms, sexe=sexe, role=role)

#         return redirect('connexion')

#     return render(request, 'comptes/inscription.html')

# def connexion_view(request):
#     if request.method == "POST":
#         login_user = request.POST['login']
#         password = request.POST['password']
        
#         user = authenticate(request, username=login_user, password=password)
#         if user is not None:
#             login(request, user)
#             if user.is_superuser:
#                 return redirect('admin_dashboard')
#             else:
#                 return redirect('vendeur_dashboard')

#     return render(request, 'comptes/connexion.html')



# comptes/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profil

def inscription_view(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenoms = request.POST.get('prenoms')
        sexe = request.POST.get('sexe')
        role = request.POST.get('role')
        login_user = request.POST.get('login')
        password = request.POST.get('password')

        # Créer un nouvel utilisateur
        user = User.objects.create_user(username=login_user, password=password)
        
        # Si le rôle est administrateur, définir is_staff à True
        if role == 'administrateur':
            user.is_staff = True
            user.save()
        
        # Créer un profil associé à cet utilisateur
        Profil.objects.create(user=user, nom=nom, prenoms=prenoms, sexe=sexe, role=role)

        return redirect('connexion')

    return render(request, 'comptes/inscription.html')

def connexion_view(request):
    if request.method == "POST":
        login_user = request.POST['login']
        password = request.POST['password']
        
        user = authenticate(request, username=login_user, password=password)
        if user is not None:
            login(request, user)
            # Récupérer le profil de l'utilisateur
            try:
                profil = Profil.objects.get(user=user)
                
                # Rediriger en fonction du rôle
                if profil.role == 'administrateur':
                    return redirect('admin_dashboard')
                elif profil.role == 'vendeur':
                    return redirect('vendeur_dashboard')
            except Profil.DoesNotExist:
                # Gérer le cas où aucun profil n'est trouvé
                return redirect('connexion')

    return render(request, 'comptes/connexion.html')