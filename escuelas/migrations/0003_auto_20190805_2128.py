# Generated by Django 2.2.4 on 2019-08-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0002_auto_20190805_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='entidadconvocatoria',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]