# Generated by Django 2.2.4 on 2019-08-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agua', '0003_auto_20190806_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='analisis',
            name='evidencia_visita',
            field=models.FileField(blank=True, null=True, upload_to='evidencia_visita/%Y/%m/%d/', verbose_name='Evidencia de visita'),
        ),
    ]