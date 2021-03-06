# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-18 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(blank=True, max_length=30)),
                ('cantidad', models.CharField(blank=True, max_length=30)),
                ('precio_unitario', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_total', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=30, null=True)),
                ('opservacion', models.TextField(blank=True, null=True)),
                ('articulo1', models.CharField(blank=True, max_length=30)),
                ('cantidad1', models.CharField(blank=True, max_length=30)),
                ('precio_unitario1', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_total1', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion1', models.CharField(blank=True, max_length=30, null=True)),
                ('opservacion1', models.TextField(blank=True, null=True)),
                ('articulo2', models.CharField(blank=True, max_length=30)),
                ('cantidad2', models.CharField(blank=True, max_length=30)),
                ('precio_unitario2', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_total2', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion2', models.CharField(blank=True, max_length=30, null=True)),
                ('opservacion2', models.TextField(blank=True, null=True)),
                ('articulo3', models.CharField(blank=True, max_length=30)),
                ('cantidad3', models.CharField(blank=True, max_length=30)),
                ('precio_unitario3', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_total3', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion3', models.CharField(blank=True, max_length=30, null=True)),
                ('opservacion3', models.TextField(blank=True, null=True)),
                ('articulo4', models.CharField(blank=True, max_length=30)),
                ('cantidad4', models.CharField(blank=True, max_length=30)),
                ('precio_unitario4', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_total4', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion4', models.CharField(blank=True, max_length=30, null=True)),
                ('opservacion4', models.TextField(blank=True, null=True)),
                ('articulo5', models.CharField(blank=True, max_length=30)),
                ('cantidad5', models.CharField(blank=True, max_length=30)),
                ('precio_unitario5', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_total5', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion5', models.CharField(blank=True, max_length=30, null=True)),
                ('opservacion5', models.TextField(blank=True, null=True)),
                ('articulo6', models.CharField(blank=True, max_length=30)),
                ('cantidad6', models.CharField(blank=True, max_length=30)),
                ('precio_unitario6', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_total6', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion6', models.CharField(blank=True, max_length=30, null=True)),
                ('opservacion6', models.TextField(blank=True, null=True)),
                ('articulo7', models.CharField(blank=True, max_length=30)),
                ('cantidad7', models.CharField(blank=True, max_length=30)),
                ('precio_unitario7', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_total7', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion7', models.CharField(blank=True, max_length=30, null=True)),
                ('opservacion7', models.TextField(blank=True, null=True)),
                ('articulo8', models.CharField(blank=True, max_length=30)),
                ('cantidad8', models.CharField(blank=True, max_length=30)),
                ('precio_unitario8', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_total8', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion8', models.CharField(blank=True, max_length=30, null=True)),
                ('opservacion8', models.TextField(blank=True, null=True)),
                ('articulo9', models.CharField(blank=True, max_length=30)),
                ('cantidad9', models.CharField(blank=True, max_length=30)),
                ('precio_unitario9', models.CharField(blank=True, max_length=30, null=True)),
                ('precio_total9', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcion9', models.CharField(blank=True, max_length=30, null=True)),
                ('observacion9', models.TextField(blank=True, null=True)),
                ('total', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_creacion', models.DateField()),
                ('clientes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('miempresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa_a')),
            ],
        ),
    ]
