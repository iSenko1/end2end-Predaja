from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("summary/", views.summary, name="summary"),
    path("upisivanje/", views.upisivanje, name="upisivanje"),
    path("zaposlenik/<int:pk>/", views.zaposlenik, name="zaposlenik"),
    path("azuriraj/<int:pk>/", views.azuriranje, name="azuriraj"),
    path("brisanje/<int:pk>/", views.obrisiZap, name="brisanje"),
    path("odmor-zap/<int:pk>/", views.odmorZap, name="odmor-zap"),
]
