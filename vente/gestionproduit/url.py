
from django.urls import path
from gestionproduit.views import home,detail,contact,categorie,chaussure,maillot,seach,checkout,confirmation

urlpatterns = [
  path('home',home,name='home'),
  path('detail/<int:my>',detail,name='detail'),
  path('celest',contact,name='contact'),
  path('categorie',categorie,name='categorie'),
  path('chaussure',chaussure,name='chaussure'),
  path('maillot',maillot,name='maillot'),
  path('search',seach,name='search'),
  path('checkout',checkout,name='checkout'),
  path('confirmation',confirmation,name='confirmation')
]
