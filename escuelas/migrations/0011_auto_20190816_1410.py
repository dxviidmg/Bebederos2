# Generated by Django 2.2.4 on 2019-08-16 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0010_auto_20190815_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidadconvocatoria',
            name='entidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuelas.Entidad'),
        ),
    ]