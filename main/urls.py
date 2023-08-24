from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name ="home"),
path("regions/", views.regions, name ="regions"),
path("test/", views.test, name ="test"),
# path("<str:pokemon>", views.pokedex, name="home"),
path("choosedex/", views.choosedex, name ="choosedex"),
path('pokedex/<str:region>/', views.pokedex, name='pokedex'),

path("kanto/", views.kanto, name ="kanto"),
path("johto/", views.johto, name ="johto"),
path("hoenn/", views.hoenn, name ="hoenn"),
path("sinnoh/", views.sinnoh, name ="sinnoh"),
path("unova/", views.unova, name ="unova"),
path("kalos/", views.kalos, name ="kalso"),
path("alola/", views.alola, name ="alola"),
path("galar/", views.galar, name ="galar"),
path("paldea/", views.paldea, name ="paldea"),
]