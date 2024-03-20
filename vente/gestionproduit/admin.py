from django.contrib import admin
from gestionproduit.models import Categories,Produit,commentaire,Page_contact,commande

class liste1(admin.ModelAdmin):
    liste_display=('nom')

class liste(admin.ModelAdmin):
    list_display=('nom','prix','categorie','date')
    search_fields=('categorie',)
    list_editable=('prix',)
class comment(admin.ModelAdmin):
    list_display=('auteur','datepub','contenu','adresse')

class liste_contact(admin.ModelAdmin):
    list_display=('name','email','phone','message')

class commander(admin.ModelAdmin):
    list_display=('item','total','nom','adresse','tel','date_commande')

admin.site.site_header="Site de vente"
admin.site.index_title="Ecommerce"
admin.site.register(Categories,liste1)
admin.site.register(Produit,liste)
admin.site.register(commentaire,comment)
admin.site.register(Page_contact,liste_contact)
admin.site.register(commande,commander)




