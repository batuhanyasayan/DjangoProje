from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Musteri():
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    isim = models.CharField(max_length=100)
    soyisim = models.CharField(max_length=100)
    dogum_tarihi = models.DateField()
    email = models.EmailField()
    cep_telefonu = models.CharField(max_length=25)
    

    ERKEK = 'Erkek'
    KADIN = 'Kadın'
    
    CINSIYET_CHOICES = (
        (ERKEK,'Erkek'),
        (KADIN, 'Kadın')
    )
    
    cinsiyet = models.CharField(max_length=10, choices=CINSIYET_CHOICES, default=ERKEK)
    
    def __str__(self):
        return self.isim