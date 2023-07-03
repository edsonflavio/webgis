from django.urls import path

from WebGis import views

urlpatterns = [
    path('', views.index, name='index'),
    path('webgis', views.index, name='index'),
    path('webgis/map', views.home, name='home'),
    path('webgis/atualizar', views.update_ocorrencia, name='atualizar' ),
    path('webgis/listar', views.list_ocorrencia, name='listar' ),
    path('webgis/registrar', views.create_ocorrencia, name='registrar' ),
    path('webgis/coordenadas', views.ocorrencia_form, name='ocorrencia_form' ),
]