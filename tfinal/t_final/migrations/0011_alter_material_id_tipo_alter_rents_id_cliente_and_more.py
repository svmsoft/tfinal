# Generated by Django 4.1 on 2022-09-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_final', '0010_alter_material_id_tipo_alter_rents_id_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='id_tipo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rents',
            name='id_cliente',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rents',
            name='id_material',
            field=models.IntegerField(),
        ),
    ]