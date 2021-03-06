# Generated by Django 4.0.1 on 2022-02-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0021_alter_ingreso_guias_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso_guias',
            name='boleta_cte',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Boleta Contra Entrega'),
        ),
        migrations.AlterField(
            model_name='ingreso_guias',
            name='comision',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Comision'),
        ),
        migrations.AlterField(
            model_name='ingreso_guias',
            name='ptpae',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Precio Total Del Envio'),
        ),
    ]
