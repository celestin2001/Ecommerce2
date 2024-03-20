from django import forms
from .models import commentaire

class rowform(forms.ModelForm):

    class Meta:
        model=commentaire
        fields=['auteur','contenu','adresse']
    
       