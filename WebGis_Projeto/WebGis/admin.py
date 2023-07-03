from django.contrib import admin
from django.db import models
#from . import models
from WebGis import models
# Register your models here.

admin.site.register(models.Ocorrencia)
admin.site.register(models.TipoOcorrencia)
admin.site.register(models.RegistroOcorrencia)
