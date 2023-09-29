from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
    
    kurs = Kurs.objects.filter(
        Q(is_web=True) |
        Q(is_program=True) 
        )
    context = {
        
        'kurs': kurs,
    }
    
    return render (request, 'index.html', context)

#*Kursun Detay Sayfasına Gider
def kurs_detay(request, slug):
    kurs = Kurs.objects.filter(slug=slug)
    
    context = {
        'kurs': kurs,
        
    }
    
    return render(request, 'kurs-detay.html', context)

#* ana kategori içerisinde bulunan tüm elemanları görüntüler
def kategori_detay(request, slug):
    
    kategoriler = Kategori.objects.filter(parent__slug = slug)
    kurs =[]
    for i in kategoriler:
        alt_kategoriler = i.kurs_set.filter(is_active = True)
        kurs.extend(alt_kategoriler)
    
    context = {
        
        'kurs': kurs,
    }
    return render(request, 'kategori-detay.html', context)

def kategori_alt_detay(request, slug):
    
    kurs = Kurs.objects.filter(kategori__slug = slug)
    context = {
        
        'kurs': kurs,
    }
    
    return render(request, 'kurs-alt-detay.html', context)

def search(request):
    kurs = Kurs.objects.filter(
        Q(is_web = True)|
        Q(is_program = True)
    )
    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        kurs = Kurs.objects.filter(
            Q(isim__icontains  = search)|
            Q(kisa_aciklama__icontains = search)
        )
    if not kurs.exists():
        return redirect('bos-sayfa')
    context = {
        'search': search,
        'kurs': kurs
    }
    return render(request, 'search.html', context)
    
def search_bos(request):
    
    return render(request, 'bos.html')