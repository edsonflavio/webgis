# Generated by Django 4.1.9 on 2023-07-07 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebGis', '0003_registroservico_descricao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registroservico',
            options={'ordering': ['data_registro'], 'verbose_name': 'Registro das Ocorrências', 'verbose_name_plural': 'registro_servicos'},
        ),
    ]
