# Generated by Django 3.2.8 on 2021-11-07 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_anualista_finalidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diarista',
            name='finalidade',
        ),
        migrations.RemoveField(
            model_name='mensalista',
            name='finalidade',
        ),
    ]