# Generated by Django 2.2.4 on 2019-08-16 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0018_oficio'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuela',
            name='lista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escuelas.Oficio'),
        ),
    ]
