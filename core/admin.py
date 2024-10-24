from django.contrib import admin

from .models import(
    Cor, Uva, Vinho
)

admin.site.register(Cor)
admin.site.register(Uva)
admin.site.register(Vinho)

class CorAdmin(admin.ModelAdmin):
    list_display = (
        'nome'
    )
    
    
class UvaAdmin(admin.ModelAdmin):
    list_display = (
        'nome'
    )    
    
class VinhoAdmin(admin.ModelAdmin):
    list_display = (
        'nome'
    )    