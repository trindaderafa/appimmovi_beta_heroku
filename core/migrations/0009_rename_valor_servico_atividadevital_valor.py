# Generated by Django 3.2.8 on 2021-11-14 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_valor_licenca_atividadevital_valor_servico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividadevital',
            old_name='valor_servico',
            new_name='valor',
        ),
    ]
