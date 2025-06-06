# Generated by Django 4.0.3 on 2022-04-11 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20211121_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividadeano',
            name='finalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.finalidade', verbose_name='serviço'),
        ),
        migrations.AlterField(
            model_name='atividadedia',
            name='finalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.finalidade', verbose_name='serviço'),
        ),
        migrations.AlterField(
            model_name='atividademes',
            name='finalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.finalidade', verbose_name='serviço'),
        ),
        migrations.AlterField(
            model_name='atividademes',
            name='valor_mes',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='atividadevital',
            name='finalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.finalidade', verbose_name='serviço'),
        ),
    ]
