# Generated by Django 4.0.1 on 2022-02-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0022_alter_ingreso_guias_boleta_cte_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso_guias',
            name='codigo_cliente',
            field=models.CharField(max_length=8),
        ),
    ]