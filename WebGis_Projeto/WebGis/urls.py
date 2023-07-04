from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from WebGis import views
from WebGis.views import IndexTemplateView, RegistroOcorrenciaView, ListaServicos, ListaCategorias, ListaRegistros

urlpatterns = [
#    path('', views.index, name='index'),
#    path('webgis', views.index, name='index'),
#    path('webgis/map', views.home, name='home'),
#    path('webgis/atualizar', views.update_ocorrencia, name='atualizar' ),
#    path('webgis/listar', views.list_ocorrencia, name='listar' ),
#    path('webgis/registrar', views.create_ocorrencia, name='registrar' ),
#    path('webgis/coordenadas', views.ocorrencia_form, name='ocorrencia_form' ),
    path('', IndexTemplateView.as_view(), name='index'),
    path('servicos', ListaServicos.as_view(), name='lista-servico'),
    path('categorias', ListaCategorias.as_view(), name='lista-categorias'),
    path('registros', ListaRegistros.as_view(), name='lista-registros'),
    path('ocorrencia', RegistroOcorrenciaView.as_view(), name='ocorrencia' ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)