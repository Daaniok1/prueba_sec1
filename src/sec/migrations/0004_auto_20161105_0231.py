# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-05 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0003_auto_20161105_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='horas_practicas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='horas_teoricas',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asignatura',
            name='nivel',
            field=models.IntegerField(choices=[(1, b'1er Semestre'), (2, b'2do Semestre'), (3, b'3er Semestre'), (4, b'4to Semestre'), (5, b'5to Semestre'), (6, b'6to Semestre'), (7, b'7mo Semestre'), (8, b'8vo Semestre')], default=1),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='asignatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sec.asignatura'),
        ),
    ]
