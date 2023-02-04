from django.contrib import admin
from .models import Services


#Clase para configuracion extendida al administrador crearlo con el nombre del modelo + admin
class ServicesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') #solo se visualizan los campos que se especifica, de solo lectura

# Register your models here.
admin.site.register(Services)

