# Generated by Django 3.2.8 on 2021-11-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_atividadevital_vitalista'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametro',
            name='valor_licenca',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]