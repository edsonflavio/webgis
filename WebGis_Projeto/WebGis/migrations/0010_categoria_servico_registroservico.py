# Generated by Django 4.1.9 on 2023-07-06 14:54

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebGis', '0009_alter_ocorrencia_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebGis.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_origem', models.GenericIPAddressField()),
                ('data_registro', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('ponto', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('endereco', models.CharField(blank=True, max_length=200, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebGis.servico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]