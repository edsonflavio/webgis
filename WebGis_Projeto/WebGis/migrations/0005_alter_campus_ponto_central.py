# Generated by Django 4.1.9 on 2023-07-08 10:10

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebGis', '0004_alter_registroservico_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='ponto_central',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, null=True, srid=4326, verbose_name='Centróide do Campus'),
        ),
    ]
