from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from WebGis.models import ReporteUsuario, UnidadeGestora, Servico, Categoria, Campus, RegistroServico

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton

class ReporteUsuarioInline(admin.StackedInline):
    model = ReporteUsuario
    can_delete = False
    verbose_name_plural = "reporte_usuarios"

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ReporteUsuarioInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Servico)
admin.site.register(RegistroServico)
admin.site.register(Categoria)
admin.site.register(Campus)
admin.site.register(UnidadeGestora)