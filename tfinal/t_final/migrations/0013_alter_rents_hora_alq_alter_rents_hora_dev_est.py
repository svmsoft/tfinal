# Generated by Django 4.1 on 2022-09-29 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_final', '0012_alter_material_id_tipo_alter_rents_id_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rents',
            name='hora_alq',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rents',
            name='hora_dev_est',
            field=models.CharField(max_length=20),
        ),
    ]
