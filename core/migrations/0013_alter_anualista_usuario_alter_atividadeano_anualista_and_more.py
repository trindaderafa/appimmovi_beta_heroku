# Generated by Django 4.0.4 on 2022-06-14 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_atividadeano_finalidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anualista',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pessoa'),
        ),
        migrations.AlterField(
            model_name='atividadeano',
            name='anualista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.anualista'),
        ),
        migrations.AlterField(
            model_name='atividadeano',
            name='finalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.finalidade', verbose_name='serviço'),
        ),
        migrations.AlterField(
            model_name='atividadedia',
            name='diarista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.diarista'),
        ),
        migrations.AlterField(
            model_name='atividadedia',
            name='finalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.finalidade', verbose_name='serviço'),
        ),
        migrations.AlterField(
            model_name='atividademes',
            name='finalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.finalidade', verbose_name='serviço'),
        ),
        migrations.AlterField(
            model_name='atividademes',
            name='mensalista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mensalista'),
        ),
        migrations.AlterField(
            model_name='atividadevital',
            name='finalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.finalidade', verbose_name='serviço'),
        ),
        migrations.AlterField(
            model_name='atividadevital',
            name='vitalista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vitalista'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pessoa'),
        ),
        migrations.AlterField(
            model_name='mensalista',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pessoa'),
        ),
        migrations.AlterField(
            model_name='vitalista',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pessoa'),
        ),
    ]