from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name ="home"),
path("regions/", views.regions, name ="regions"),
path("test/", views.test, name ="test"),
# path("<str:pokemon>", views.pokedex, name="home"),
path("choosedex/", views.choosedex, name ="choosedex"),
path('pokedex/<str:region>/', views.pokedex, name='pokedex'),

path("kanto/<str:region>/", views.kanto, name='kanto'),
path("johto/<str:region>/", views.johto, name ="johto"),
path("hoenn/<str:region>/", views.hoenn, name ="hoenn"),
path("sinnoh/<str:region>/", views.sinnoh, name ="sinnoh"),
path("unova/<str:region>/", views.unova, name ="unova"),
path("kalos/<str:region>/", views.kalos, name ="kalos"),
path("alola/<str:region>/", views.alola, name ="alola"),
path("galar/<str:region>/", views.galar, name ="galar"),
path("paldea/<str:region>/", views.paldea, name ="paldea"),
]