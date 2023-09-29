from django.contrib import admin
from .models import *
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.utils.safestring import mark_safe

# Register your models here.

class MyDraggableMPTTAdmin(DraggableMPTTAdmin):
    readonly_fields = ('slug',)
    list_display = ('tree_actions', 'something',)
    list_display_links = ('something',)
    
    def something(self, instance):
        return format_html(
            '<div style="text-indent: {}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.isim,
        )
        
class KursAdmin(admin.ModelAdmin):
    list_display = ('isim', 'is_web', 'is_program', 'is_active', 'secilen_kategori',)
    list_editable = ('is_web', 'is_program', 'is_active',)
    list_filter = ('is_web', 'is_program', 'is_active', 'kategori',)
    readonly_fields = ('slug',)
    
    def secilen_kategori(self, obj):
        kategori_list = obj.kategori.all()
        parent_list = []
        for kategori in kategori_list:
            parent = kategori.parent
            if parent:
                parent_list.append(parent.isim)
        if parent_list:
            ul_html = "<ul>"
            for parent in parent_list:
                ul_html += f"<li>{parent}</li>"
            ul_html += "</ul>"
            return mark_safe(ul_html)
        else:
            return "-"
        
class AdresAdmin(admin.ModelAdmin):
    list_display = ('ulke', 'sehir', 'ilce', 'acik_adres', 'adres_baslik',)
    list_filter = ('ulke', 'sehir', 'ilce', 'acik_adres', 'adres_baslik',)
    search_fields = ['ulke', 'sehir', 'ilce', 'acik_adres', 'adres_baslik',]
    

admin.site.register(Kategori,MyDraggableMPTTAdmin)
admin.site.register(Kurs, KursAdmin)
admin.site.register(Musteri)
admin.site.register(Adres, AdresAdmin)