# Generated by Django 4.1 on 2022-09-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_final', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rents',
            name='importe',
            field=models.FloatField(default=0),
        ),
    ]
