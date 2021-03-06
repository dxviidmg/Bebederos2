# Generated by Django 2.2.4 on 2019-08-05 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EntidadConvocatoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escuelas_asignadas', models.IntegerField()),
                ('escuelas_registradas', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
                ('convocatoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuelas.Convocatoria')),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuelas.Entidad')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('cct', models.CharField(max_length=10)),
                ('nombre', models.TextField()),
                ('nivel_educativo', models.CharField(choices=[('Preescolar', 'Preescolar'), ('Primaria', 'Primaria'), ('Secundaria', 'Secundaria')], max_length=20)),
                ('turno', models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Tiempo Completo', 'Tiempo Completo')], default='Matutino', max_length=20)),
                ('plantilla_escolar', models.IntegerField()),
                ('municipio', models.CharField(max_length=50)),
                ('domicilio', models.TextField()),
                ('localidad', models.CharField(max_length=50)),
                ('director', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('esta_sustituida', models.BooleanField(default=False)),
                ('es_sustitucion', models.BooleanField(default=False)),
                ('entidad_convocatoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuelas.EntidadConvocatoria')),
            ],
        ),
        migrations.AddField(
            model_name='entidad',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuelas.Region', verbose_name='Región'),
        ),
    ]
