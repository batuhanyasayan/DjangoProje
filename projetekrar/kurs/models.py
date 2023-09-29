from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Kategori(MPTTModel):
    isim = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, db_index=True, editable=False)
    
    class MPTTMeta:
        level_attr = 'mptt-level'
        order_insertion_by = ['isim']
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)
        
    def __str__(self):
        full_path = [self.isim]
        k = self.parent
        while k is not None:
            full_path.append(k.isim)
            k = k.parent
        return '>'.join(full_path[::-1])
    
class Kurs(models.Model):
    isim = models.CharField(max_length=100)
    kategori = models.ManyToManyField(Kategori)
    resim = models.FileField(blank=True, upload_to='kurs/', verbose_name='Kurs Resmi')
    kisa_aciklama = models.TextField(max_length=500)
    aciklama = RichTextField()
    slug = models.SlugField(null=True, blank=True, db_index=True, editable=False, unique=True) 
    is_active = models.BooleanField(default=False)
    is_web = models.BooleanField(default=False)
    is_program = models.BooleanField(default=False)
    
    def __str__(self):
        return self.isim
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)
        
class Adres(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    ulke = models.CharField(max_length=100)
    sehir = models.CharField(max_length=100)
    ilce = models.CharField(max_length=100)
    acik_adres = models.CharField(max_length=100)
    adres_baslik = models.CharField(max_length=100)
    
    def __str__ (self):
        return self.ulke
        
class Musteri(models.Model):
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
