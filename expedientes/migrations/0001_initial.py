# Generated by Django 2.2.4 on 2019-08-06 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('escuelas', '0006_auto_20190806_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acta_ubicacion', models.FileField(blank=True, null=True, upload_to='visita/actas/%Y/%m/%d/', verbose_name='Acta de ubicación de bebedero')),
                ('acta_inicio_construccion', models.FileField(blank=True, null=True, upload_to='visita/actas/%Y/%m/%d/', verbose_name='Acta de inicio de construcción')),
                ('cedula_identificacion', models.FileField(blank=True, null=True, upload_to='visita/cedulas/%Y/%m/%d/', verbose_name='Cédula de identificación')),
                ('convenio_concertacion', models.FileField(blank=True, null=True, upload_to='visitas/concertaciones/%Y/%m/%d/', verbose_name='Convenio de concertación de aplicación de recurso')),
                ('plano_conjunto', models.FileField(blank=True, null=True, upload_to='visitas/planosConjunto/%Y/%m/%d/', verbose_name='Plano de conjunto')),
                ('distribucion_planta', models.FileField(blank=True, null=True, upload_to='visitas/distribuciones/%Y/%m/%d/', verbose_name='Distribución en planta')),
                ('memoria_calculo_1', models.FileField(blank=True, null=True, upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name='Memoria de cálculo hidráulico')),
                ('memoria_calculo_2', models.FileField(blank=True, null=True, upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name='Memoria de cálculo sanitario')),
                ('memoria_calculo_3', models.FileField(blank=True, null=True, upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name='Memoria de cálculo eléctrico')),
                ('isometrico_instalacion', models.FileField(blank=True, null=True, upload_to='visitas/pihs/%Y/%m/%d/', verbose_name='Isometricos de instalaciones')),
                ('levantamiento_instalacion', models.FileField(blank=True, null=True, upload_to='visitas/pihs/%Y/%m/%d/', verbose_name='Levantamiento de instalación')),
                ('acta_funcionamiento', models.FileField(blank=True, null=True, upload_to='funcionamiento/actas/%Y/%m/%d/', verbose_name='Acta de Inicio de funcionamiento')),
                ('acta_entrega', models.FileField(upload_to='entrega/actas/%Y/%m/%d/', verbose_name='Acta de entrega')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuelas.Escuela')),
            ],
        ),
    ]
