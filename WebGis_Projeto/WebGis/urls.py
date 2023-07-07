from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from WebGis.views import (
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView,
    ServicoCreateView, ServicoUpdateView, ServicoDeleteView, ServicoListView,
    RegistroServicoCreateView, RegistroServicoUpdateView, RegistroServicoDeleteView,
    RegistroServicoListView, RegistroServicoDetailView, IndexTemplateView
)

app_name = 'WebGis'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('categoria/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/create/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/update/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/delete/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('servico/', ServicoListView.as_view(), name='servico_list'),
    path('servico/create/', ServicoCreateView.as_view(), name='servico_create'),
    path('servico/update/<int:pk>/', ServicoUpdateView.as_view(), name='servico_update'),
    path('servico/delete/<int:pk>/', ServicoDeleteView.as_view(), name='servico_delete'),
    path('registro_servico/create/', RegistroServicoCreateView.as_view(), name='registro_servico_create'),
    path('registro_servico/update/<int:pk>/', RegistroServicoUpdateView.as_view(), name='registro_servico_update'),
    path('registro_servico/delete/<int:pk>/', RegistroServicoDeleteView.as_view(), name='registro_servico_delete'),
    path('registro_servico/', RegistroServicoListView.as_view(), name='registro_servico_list'),
    path('registro_servico/detail/<int:pk>/', RegistroServicoDetailView.as_view(), name='registro_servico_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)