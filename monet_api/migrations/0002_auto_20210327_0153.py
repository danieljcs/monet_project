# Generated by Django 3.1.3 on 2021-03-27 06:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monet_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controldetalle',
            name='ciclo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='controldetalle',
            name='cuenta_bancaria_pagador',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='controldetalle',
            name='fecha_vencimiento',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(99999999)]),
        ),
        migrations.AlterField(
            model_name='controldetalle',
            name='indicador_validacion',
            field=models.CharField(blank=True, choices=[('S', 'SI'), ('N', 'NO')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='controldetalle',
            name='nit_entidad_pagador',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='controldetalle',
            name='nombre_entidad_pagador',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='controldetalle',
            name='numero_cuenta',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='controldetalle',
            name='periodos_facturados',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='controldetalle',
            name='referencia_1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='controldetalle',
            name='referencia_2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='controldetalle',
            name='tipo_transaccion',
            field=models.CharField(blank=True, choices=[(57, 'Cuenta Corriente'), (67, 'Cuenta Ahorros'), (77, 'TC VISA'), (87, 'TC MASTER'), (97, 'AMEX')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='controlregistro',
            name='nombre_entidad_recaudador',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
