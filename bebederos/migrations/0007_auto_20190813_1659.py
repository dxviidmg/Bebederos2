# Generated by Django 2.2.4 on 2019-08-13 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0006_sistemabebedero_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sistemabebedero',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]