# Generated by Django 4.0.1 on 2022-02-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0026_ingreso_hijas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso_hijas',
            name='guia_madre',
            field=models.CharField(max_length=6, verbose_name='Guia Madre'),
        ),
    ]