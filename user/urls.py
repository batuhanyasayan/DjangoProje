from django.urls import path
from .views import *

urlpatterns = [
    path('hesap-olustur/', userRegister, name='hesap-olustur'),
    path('giris-yap/', userLogin, name='giris-yap'),
    path('cikis-yap', userLogout, name='cikis-yap'),
    path('hesabim-bilgi/', hesabimBilgiler, name='hesabim-bilgi'),
    path('hesabim-sifre/', sifreDegistir, name='hesabim-sifre'),
    path('hesabim-adres/', adres, name='hesabim-adres'),
]

