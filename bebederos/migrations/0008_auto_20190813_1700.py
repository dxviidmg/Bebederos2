# Generated by Django 2.2.4 on 2019-08-13 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0007_auto_20190813_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sistemabebedero',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
