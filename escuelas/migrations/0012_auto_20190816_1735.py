# Generated by Django 2.2.4 on 2019-08-16 22:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0011_auto_20190816_1410'),
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
                ('entidad_convocatoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuelas.EntidadConvocatoria')),
            ],
        ),
        migrations.AddField(
            model_name='escuela',
            name='lista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='escuelas.Oficio'),
        ),
    ]