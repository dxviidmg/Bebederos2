# Generated by Django 2.2.4 on 2019-08-16 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0020_auto_20190816_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escuela',
            name='lista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='escuelas.Oficio'),
        ),
    ]
