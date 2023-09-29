from django.urls import path
from .views import *

urlpatterns = [
    path('kurs-detay/<slug:slug>', kurs_detay, name='kurs-detay'),
    path("kategori-detay/<slug:slug>", kategori_detay, name="kategori-detay"),
    path('kategori-alt-detay/<slug:slug>', kategori_alt_detay, name='kategori-alt-detay'),
    path('search/', search, name='search'),
    path('bos-sayfa/', search_bos, name='bos-sayfa'),
]
