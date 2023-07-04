# Generated by Django 4.1.7 on 2023-07-04 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebGis', '0004_alter_ocorrencia_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoocorrencia',
            name='toc_descOcorrencia',
            field=models.CharField(default='Categoria', help_text='Descrição sucinta da Categoria', max_length=50, verbose_name='Descrição da Categoria'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tipoocorrencia',
            name='toc_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
