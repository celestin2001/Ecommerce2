from django.shortcuts import render,get_object_or_404,redirect
from .models import Produit,Categories,commentaire,Page_contact,commande
from .form import rowform

def home(request):

    user=request.user

    produit=Produit.objects.all()
    montre=Produit.objects.filter(categorie__nom='Montres').first()
    chaussure=Produit.objects.filter(categorie__nom='chaussures').first()
    maillot=Produit.objects.filter(categorie__nom='maillots').first()
    commen=commentaire.objects.all()
    
   

    form=rowform()
    if request.method=='POST':
        form=rowform(request.POST)
        if form.is_valid():
            form.save()

        form=rowform()
    context={
        'produit':produit,
        'montre':montre,
        'chaussure':chaussure,
        'maillot':maillot,
        'commen':commen,
        'form':form,
        'user':user
    }


   
    
    
    
    
        
    return render(request,'gestionproduit/index.html',context)


def detail(request,my):
    produit=get_object_or_404(Produit,id=my)
    return render(request,'gestionproduit/about.html',{"produit":produit})

def contact(request):
   if request.method =='POST':
       name=request.POST['name']
       email=request.POST['email']
       phone=request.POST['phone']
       message=request.POST['message']
       new=Page_contact.objects.create(name=name,email=email,phone=phone,message=message)
       new.save()
   
   return render(request,'gestionproduit/contact.html')

def categorie(request):

    montre=Produit.objects.filter(categorie__nom='Montres')
    context={
        'montre':montre
    }

    return render(request,'gestionproduit/jewellery.html',context)

def chaussure(request):

    chaussure=Produit.objects.filter(categorie__nom='chaussures')
    context={
        'chaussure':chaussure
    }

    return render(request,'gestionproduit/chaussure.html',context)

def maillot(request):

    maillot=Produit.objects.filter(categorie__nom='maillots')
    context={
        'maillot':maillot
    }

    return render(request,'gestionproduit/maillo.html',context)

def seach(request):

    if request.method =='GET':
        seach=request.GET.get('search')
        produit=Produit.objects.filter(nom__icontains=seach) | Produit.objects.filter(categorie__nom__icontains=seach)
        context={
            'produit':produit
        }
        return render(request,'gestionproduit/search.html',context)

    return render(request,'gestionproduit/search.html')


def checkout(request):
    if request.method =='POST':
        nom=request.POST['nom']
        email=request.POST['email']
        adresse=request.POST['adresse']
        tel=request.POST['tel']
        item=request.POST['item']
        total=request.POST['total']
        nouveau=commande(item=item ,nom=nom,total=total,email=email,adresse=adresse,tel=tel)
        nouveau.save()
        return redirect('confirmation')
      
    return render(request,'gestionproduit/checkout.html')

def confirmation(request):
    personne=commande.objects.all()[1:]
    for item in personne:
        nom=item.nom
    
    return render(request,'gestionproduit/confirmation.html',{'nom':nom})


        











