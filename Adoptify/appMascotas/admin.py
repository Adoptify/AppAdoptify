from django.contrib import admin
from appMascotas import models
# Register your models here.

class LocalidadAdmin(admin.ModelAdmin):
	pass

class EdadAdmin(admin.ModelAdmin):
	pass
	
class SexoAdmin(admin.ModelAdmin):
	pass

class RazaAdmin(admin.ModelAdmin):
	pass
	
class EspecieAdmin(admin.ModelAdmin):
	pass
	
class PublicacionAdmin(admin.ModelAdmin):
	pass
	

admin.site.register(models.Localidad,LocalidadAdmin)
admin.site.register(models.Edad,EdadAdmin)
admin.site.register(models.Sexo,SexoAdmin)
admin.site.register(models.Raza,RazaAdmin)
admin.site.register(models.Especie,EspecieAdmin)
admin.site.register(models.Publicacion,PublicacionAdmin)