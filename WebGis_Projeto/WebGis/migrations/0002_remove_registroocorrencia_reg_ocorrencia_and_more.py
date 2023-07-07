# Generated by Django 4.1.9 on 2023-07-07 15:26

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WebGis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registroocorrencia',
            name='reg_Ocorrencia',
        ),
        migrations.RemoveField(
            model_name='registroocorrencia',
            name='reg_usuarioRegistro',
        ),
        migrations.RemoveField(
            model_name='tipoocorrencia',
            name='toc_usuario',
        ),
        migrations.AddField(
            model_name='categoria',
            name='descricao',
            field=models.TextField(blank=True, help_text='Descreva sucintamente esta Categoria', max_length=200, null=True, verbose_name='Descrição da Categoria'),
        ),
        migrations.AddField(
            model_name='servico',
            name='descricao',
            field=models.TextField(blank=True, help_text='Descreva sucintamente este serviço', max_length=200, null=True, verbose_name='Descrição do Serviço'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='nome',
            field=models.CharField(db_index=True, help_text='Informe o Nome do Campus mais próximo', max_length=60, verbose_name='Nome do Campus'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(help_text='Informe o Nome da Categoria', max_length=40, verbose_name='Nome da Categoria'),
        ),
        migrations.AlterField(
            model_name='registroservico',
            name='data_alteracao',
            field=models.DateTimeField(auto_now=True, help_text='Data e Hora da Alteração do registro da Ocorrência', verbose_name='Recebe o data e hora da Alteração do Registro da Ocorrência'),
        ),
        migrations.AlterField(
            model_name='registroservico',
            name='data_registro',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Data e Hora do Registro da Ocorrência', verbose_name='Recebe o data e hora do Registro da Ocorrência'),
        ),
        migrations.AlterField(
            model_name='registroservico',
            name='foto',
            field=models.ImageField(blank=True, help_text='Foto da Ocorrência', null=True, upload_to='fotos/', verbose_name='Permite a inserção de uma Foto para Registro da Ocorrência'),
        ),
        migrations.AlterField(
            model_name='registroservico',
            name='ip_origem',
            field=models.GenericIPAddressField(help_text='Recebe o IP do Usuário', verbose_name='Endereço IP do Usuário'),
        ),
        migrations.AlterField(
            model_name='registroservico',
            name='ponto',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, help_text='Recebe as coordenadas aproximadas da Ocorrência', null=True, srid=4326, verbose_name='Localização aproximada da Ocorrência'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='nome',
            field=models.CharField(help_text='Informe o Nome do Serviço', max_length=60, verbose_name='Nome do Serviço'),
        ),
        migrations.DeleteModel(
            name='Ocorrencia',
        ),
        migrations.DeleteModel(
            name='RegistroOcorrencia',
        ),
        migrations.DeleteModel(
            name='TipoOcorrencia',
        ),
    ]
