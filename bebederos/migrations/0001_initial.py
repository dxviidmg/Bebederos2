# Generated by Django 2.2.4 on 2019-08-06 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SistemaPotabilizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('ficha_tecnica', models.FileField(blank=True, null=True, upload_to='ficha_tecnica/%Y/%m/%d/', verbose_name='Ficha técnica')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bebederos.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('rango', models.CharField(choices=[('1-300', '1-300'), ('301-400', '301-400'), ('401-600', '401-600'), ('601 o más', '601 o más')], max_length=10)),
                ('ficha_tecnica', models.FileField(blank=True, null=True, upload_to='ficha_tecnica/%Y/%m/%d/', verbose_name='Ficha técnica')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bebederos.Proveedor')),
            ],
        ),
    ]