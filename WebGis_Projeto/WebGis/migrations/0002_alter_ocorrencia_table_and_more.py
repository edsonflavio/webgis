# Generated by Django 4.1.7 on 2023-07-03 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebGis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ocorrencia',
            table='Ocorrencia',
        ),
        migrations.AlterModelTable(
            name='registroocorrencia',
            table='RegistroOcorrencia',
        ),
        migrations.AlterModelTable(
            name='tipoocorrencia',
            table='TipoOcorrencia',
        ),
    ]
