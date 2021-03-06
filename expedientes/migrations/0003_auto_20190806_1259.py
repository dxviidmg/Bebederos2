# Generated by Django 2.2.4 on 2019-08-06 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0006_auto_20190806_1446'),
        ('expedientes', '0002_auto_20190806_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='escuela',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='escuelas.Escuela'),
        ),
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotografia', models.ImageField(upload_to='fotografias/%Y/%m/%d/')),
                ('descripcion', models.CharField(choices=[('1 Antes', 'Antes'), ('2 Durante', 'Durante'), ('3 Despues', 'Despues')], max_length=10)),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuelas.Escuela')),
            ],
        ),
    ]
