# Generated by Django 2.2.4 on 2019-08-16 22:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0017_delete_oficio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('archivo', models.FileField(upload_to='mantenimientos/%Y/%m/%d/')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.CharField(max_length=50)),
                ('entidad_convocatoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escuelas.EntidadConvocatoria')),
            ],
        ),
    ]
