# Generated by Django 2.2.4 on 2019-08-16 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agua', '0004_analisis_evidencia_visita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analisis',
            old_name='aboratorio',
            new_name='laboratorio',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_arsenico',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_coliformes_fecales',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_coliformes_totales',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_color_verdadero',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_conductividad_electrica',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_dureza_total',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_floururos',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_hierro',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_manganeso',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_nitratos',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_ph',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_plomo',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_solidos_disueltos',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_sulfatos',
        ),
        migrations.RemoveField(
            model_name='analisis',
            name='comparacion_turbiedad',
        ),
    ]
