# Generated by Django 2.2.4 on 2019-08-17 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agua', '0005_auto_20190816_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictamen',
            old_name='documento',
            new_name='archivo',
        ),
    ]
