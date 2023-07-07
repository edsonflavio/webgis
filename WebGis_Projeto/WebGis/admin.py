from django.contrib import admin
from django.db import models
#from . import models
from WebGis import models
# Register your models here.

admin.site.register(models.Servico)
admin.site.register(models.RegistroServico)
admin.site.register(models.Categoria)
admin.site.register(models.Campus)

