from django.db import models

class Categories(models.Model):
    nom=models.CharField(max_length=20)


    def __str__(self):
      
       return self.nom

class Produit(models.Model):
    nom=models.CharField(max_length=30)
    prix=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='%Y%m%d')
    date=models.DateField(auto_now=True)
    categorie=models.ForeignKey(Categories,on_delete=models.CASCADE)


    def __str__(self):
        return self.nom 
    

class commentaire(models.Model):
    auteur=models.CharField(max_length=20)
    datepub=models.DateField(auto_now=True)
    contenu=models.TextField()
    adresse=models.CharField(max_length=20,default='ratoma')

    class META:
        ordering=['-datepub']

    def __str__(self):
        return self.auteur
    

class Page_contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.CharField(max_length=120)

    def __str__(self):
        return self.name
    

class commande(models.Model):
    item=models.CharField(max_length=120)
    total=models.CharField(max_length=120)
    nom=models.CharField(max_length=30)
    email=models.EmailField()
    adresse=models.CharField(max_length=128)
    tel=models.PositiveIntegerField()
    date_commande=models.DateField(auto_now=True)

    class META:
        ordoring=['-date_commande']

    def __str__(self):
        return self.item
    


    
    
    


