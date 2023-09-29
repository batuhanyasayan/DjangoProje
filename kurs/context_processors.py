from .models import *

def kategori_context(request):
    kategori = Kategori.objects.all()
    return{'kategori': kategori}
