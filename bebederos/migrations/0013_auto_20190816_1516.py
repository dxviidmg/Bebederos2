# Generated by Django 2.2.4 on 2019-08-16 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0012_auto_20190816_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sistemabebedero',
            name='escuela',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='escuela_sistemabebedero', to='escuelas.Escuela'),
        ),
    ]