from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ( TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView )
from django.contrib.gis.geos import GEOSGeometry
from geopy.geocoders import Nominatim
from WebGis.forms import ( CategoriaForm, ServicoForm, RegistroServicoForm )
from WebGis.models import ( Categoria, Servico, RegistroServico )
from django.contrib.gis.geos import Point
import exifread
import requests

class IndexTemplateView(TemplateView):
  template_name = "WebGis/index.html"

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'WebGis/categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'WebGis/categoria_form.html'
    success_url = reverse_lazy('WebGis:categoria_list')

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'WebGis/categoria_form.html'
    success_url = reverse_lazy('WebGis:categoria_list')

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'WebGis/categoria_confirm_delete.html'
    success_url = reverse_lazy('WebGis:categoria_list')

class ServicoListView(ListView):
    model = Servico
    template_name = 'WebGis/servico_list.html'
    context_object_name = 'servicos'

class ServicoCreateView(LoginRequiredMixin, CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'WebGis/servico_form.html'
    success_url = reverse_lazy('WebGis:servico_list')
    
class ServicoUpdateView(LoginRequiredMixin, UpdateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'WebGis/servico_form.html'
    success_url = reverse_lazy('WebGis:servico_list')

    def get_object(self, queryset=None):
        servico = None
        # Os campos {pk} e {slug} estão presentes em self.kwargs
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if id is not None:
            # Busca o serviço apartir do id
            servico = Servico.objects.filter(id=id).first()
        elif slug is not None:
            # Pega o campo slug do Model
            campo_slug = self.get_slug_field()
            # Busca o serviço apartir do slug
            servico = Servico.objects.filter(**{campo_slug: slug}).first()
        # Retorna o objeto encontrado
        return servico

class ServicoDeleteView(LoginRequiredMixin, DeleteView):
    model = Servico
    template_name = 'WebGis/servico_confirm_delete.html'
    success_url = reverse_lazy('WebGis:servico_list')

class RegistroServicoCreateView(LoginRequiredMixin, CreateView):
    model = RegistroServico
    form_class = RegistroServicoForm
    template_name = 'WebGis/registro_servico_form.html'
    success_url = reverse_lazy('WebGis:registro_servico_detail')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.ip_origem = self.request.META.get('REMOTE_ADDR')
        if form.cleaned_data.get('local'):
            geolocator = Nominatim(user_agent="my-app")
            location = geolocator.geocode(form.cleaned_data['local'])
            if location:
                form.cleaned_data['latitude'] = location.latitude
                form.cleaned_data['longitude'] = location.longitude
                form.cleaned_data['ponto'] = f"POINT({location.longitude} {location.latitude})"
        elif form.cleaned_data.get('foto'):
            photo = form.cleaned_data['foto']
            tags = exifread.process_file(photo.file)
            if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
                latitude_ref = str(tags['GPS GPSLatitudeRef'])
                latitude = str(tags['GPS GPSLatitude'])
                longitude_ref = str(tags['GPS GPSLongitudeRef'])
                longitude = str(tags['GPS GPSLongitude'])
                latitude = eval(latitude.replace(" ", ","))
                longitude = eval(longitude.replace(" ", ","))
                latitude = latitude[0] + latitude[1] / 60 + latitude[2] / 3600
                longitude = longitude[0] + longitude[1] / 60 + longitude[2] / 3600
                if latitude_ref == 'S':
                    latitude = -latitude
                if longitude_ref == 'W':
                    longitude = -longitude
                form.cleaned_data['latitude'] = latitude
                form.cleaned_data['longitude'] = longitude
                form.cleaned_data['ponto'] = f"POINT({longitude} {latitude})"
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url(self):
        return reverse_lazy('WebGis:registro_servico_detail', kwargs={'pk': self.object.pk})
    
class RegistroServicoUpdateView(LoginRequiredMixin, UpdateView):
    model = RegistroServico
    form_class = RegistroServicoForm
    template_name = 'WebGis/registro_servico_form.html'
    success_url = reverse_lazy('WebGis:registro_servico_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.ip_origem = self.request.META.get('REMOTE_ADDR')
        if form.cleaned_data.get('local'):
            geolocator = Nominatim(user_agent="my-app")
            location = geolocator.geocode(form.cleaned_data['local'])
            if location:
                form.cleaned_data['latitude'] = location.latitude
                form.cleaned_data['longitude'] = location.longitude
                form.cleaned_data['ponto'] = f"POINT({location.longitude} {location.latitude})"
        elif form.cleaned_data.get('foto'):
            photo = form.cleaned_data['foto']
            tags = exifread.process_file(photo.file)
            if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
                latitude_ref = str(tags['GPS GPSLatitudeRef'])
                latitude = str(tags['GPS GPSLatitude'])
                longitude_ref = str(tags['GPS GPSLongitudeRef'])
                longitude = str(tags['GPS GPSLongitude'])
                latitude = eval(latitude.replace(" ", ","))
                longitude = eval(longitude.replace(" ", ","))
                latitude = latitude[0] + latitude[1] / 60 + latitude[2] / 3600
                longitude = longitude[0] + longitude[1] / 60 + longitude[2] / 3600
                if latitude_ref == 'S':
                    latitude = -latitude
                if longitude_ref == 'W':
                    longitude = -longitude
                form.cleaned_data['latitude'] = latitude
                form.cleaned_data['longitude'] = longitude
                form.cleaned_data['ponto'] = f"POINT({longitude} {latitude})"
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url(self):
        return reverse_lazy('registro_servico_detail', kwargs={'pk': self.object.pk})
    
class RegistroServicoDeleteView(LoginRequiredMixin, DeleteView):
    model = RegistroServico
    template_name = 'WebGis/registro_servico_confirm_delete.html'
    success_url = reverse_lazy('WebGis:registro_servico_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url(self):
        return reverse_lazy('WebGis:registro_servico_detail', kwargs={'pk': self.object.pk})
    
class RegistroServicoListView(ListView):
    model = RegistroServico
    #paginate_by = 10
    template_name = 'WebGis/registro_servico_list.html'
    context_object_name = 'registro_servicos'

class RegistroServicoDetailView(DetailView):
    model = RegistroServico
    template_name = 'WebGis/registro_servico_detail.html'
    context_object_name = 'registro_servicos'