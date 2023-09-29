from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from kurs.models import *

# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        isim = request.POST['isim']
        soyisim = request.POST['soyisim']
        dogumtarihi = request.POST['dogumtarihi']
        email = request.POST['email']
        sifre = request.POST['sifre']
        telefon = request.POST['telefon']
        cinsiyet = request.POST['cinsiyet'] 
        
        if User.objects.filter(email = email).exists():
            messages.error(request, 'Bu email zaten kullanılıyor')
            return redirect('hesap-olustur')
        else:
            user = User.objects.create_user(
                username = email,email = email, first_name = isim, last_name = soyisim, password = sifre
            )
            musteri = Musteri.objects.create(
                user = user, isim = isim, soyisim = soyisim, email = email, dogum_tarihi = dogumtarihi, cinsiyet = cinsiyet, cep_telefonu = telefon
            )
            musteri.save()
            user.save()
            messages.success(request, 'Kullanıcı Oluşturuldu')
            return redirect('giris-yap')
    else:
        return render(request, 'hesapolustur.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Yapıldı')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre yanlış. Tekrar deneyiniz!')
            return redirect('giris-yap')
        
    return render(request, 'girisyap.html')

def userLogout(request):
    logout(request)
    messages.error(request, 'Çıkış Yapıldı')
    return redirect('giris-yap')

def hesabimBilgiler(request):
    
    if request.method == 'POST':
        yeni_isim = request.POST['isim']
        yeni_soyisim = request.POST['soyisim']
        yeni_dogumtarihi = request.POST['dogumtarihi']
        yeni_cinsiyet = request.POST['cinsiyet']
        
        user = request.user
        musteri = Musteri.objects.get(user=user)
        user.firt_name = yeni_isim
        user.last_name = yeni_soyisim
        musteri.isim = yeni_isim
        musteri.soyisim = yeni_soyisim
        musteri.dogum_tarihi = yeni_dogumtarihi
        musteri.cinsiyet = yeni_cinsiyet
        
        musteri.save()
        user.save()
        
        messages.success(request, 'Kullanıcı Bilgileri Başarı İle Güncellendi!')
        return redirect('hesabim-bilgi')
    
    return render(request, 'hesabim-bilgileri.html')

def sifreDegistir(request):
    
    if request.method == 'POST':
        mevcut_sifre = request.POST['mevcut-sifre']
        yeni_sifre = request.POST['yeni-sifre']
        yeni_sifre_tekrar = request.POST['yeni-sifre-tekrar']
        
        user = request.user
        if user.check_password(mevcut_sifre):
            if yeni_sifre == yeni_sifre_tekrar:
                user.set_password(yeni_sifre)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Şifre Başarıyla Güncellendi')
                return redirect('hesabim-sifre')
        else:
            messages.error(request, 'Mevcut Şifre Yanlış Girildi veya Yeni Şifreler Eşleşmiyor.')
            return redirect('hesabim-sifre')
        
    return render(request, 'hesabim-sifre-degistir.html')

def adres(request):
    
    if request.method == 'POST':
        ulke = request.POST['ulke']
        sehir = request.POST['sehir']
        ilce = request.POST['ilce']
        acik_adres = request.POST['acik-adres']
        adres_baslik = request.POST['adres-baslik']
        
        user = request.user
        
        try:
            adres = Adres.objects.get(user=user)
            adres.ulke = ulke
            adres.sehir = sehir
            adres.ilce = ilce
            adres.acik_adres = acik_adres
            adres.adres_baslik = adres_baslik
            adres.save()
            
        except Adres.DoesNotExist:
            adres = Adres.objects.create(
                user = user,
                ulke = ulke,
                sehir = sehir,
                ilce = ilce,
                acik_adres = acik_adres,
                adres_baslik = adres_baslik
            )
            adres.save()
        return redirect('hesabim-adres')
    
    user = request.user
    adress = Adres.objects.filter(user = user)
    context = {
        'adress': adress,
    }
    
    return render(request, 'hesabim-adres.html', context)