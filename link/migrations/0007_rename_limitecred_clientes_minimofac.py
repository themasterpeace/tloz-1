# Generated by Django 4.0.1 on 2022-02-04 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0006_rename_nombre_clientes_nombrecom_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='limitecred',
            new_name='minimofac',
        ),
    ]