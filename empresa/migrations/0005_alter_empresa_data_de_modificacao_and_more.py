# Generated by Django 4.2.6 on 2023-11-21 20:28

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("empresa", "0004_alter_empresa_data_de_modificacao_projeto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="data_de_modificacao",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 21, 20, 28, 14, 665639, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="projeto",
            name="data_de_pedido",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]