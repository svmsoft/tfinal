# Generated by Django 4.1 on 2022-10-01 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_final', '0015_clientes_activo_material_activo_tipo_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=50)),
                ('permiso', models.CharField(max_length=50)),
                ('activo', models.CharField(max_length=5, null=True)),
            ],
        ),
    ]
