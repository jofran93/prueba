from django.contrib import admin

from visitApp import models

admin.site.register(models.Comunidad)
admin.site.register(models.Propietario)
admin.site.register(models.Administrador)
admin.site.register(models.Usuario)
admin.site.register(models.Visita)

# Register your models here.
