# Generated by Django 2.2.4 on 2019-08-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0005_auto_20190813_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='sistemabebedero',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]