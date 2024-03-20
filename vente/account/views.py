from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def signup(request):
   if request.method =='POST':
     username=request.POST['username']
     email=request.POST['email']
     password=request.POST['password']
     valid_nom=User.objects.filter(username=username)
     if valid_nom:
        messages.error(request,'ce nom existe deja')
        return render(request,'account/signup.html')
     valid_email=User.objects.filter(email=email)
     if valid_email:
        messages.error(request,'cet email existe deja')
        return render(request,'account/signup.html')
     if len(password)<7:
        messages.error(request,'le mot de passe doit contenir plus de huit caractères')
        return render(request,'account/signup.html')
     new=User.objects.create_user(username,email,password)
     new.save()
     messages.success(request,'felicitation votre compte à été créer avec succès connectez vous donc')
     return render(request,'account/connexion.html')
     

   return render(request,'account/signup.html')

def connexion(request):
   if request.method=='POST':
      username=request.POST['utilisateur']
      password=request.POST['passworde']
      user=authenticate(request,username=username,password=password)
      if user is not None:
         login(request,user)
         return render(request,'gestionproduit/index.html')
      else:
         messages.error(request,'vos informations ne sont pas conforme')
         return render(request,'account/connexion.html')
      
   return render(request,'account/connexion.html')



       




