# Generated by Django 2.2.4 on 2019-08-06 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuelas', '0007_auto_20190806_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='abreviatura',
            field=models.CharField(max_length=4),
        ),
    ]
