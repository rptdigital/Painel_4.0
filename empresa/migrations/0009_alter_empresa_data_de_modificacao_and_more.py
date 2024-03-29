# Generated by Django 4.2.6 on 2023-11-22 20:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("empresa", "0008_remove_projeto_servico_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="data_de_modificacao",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 22, 20, 51, 29, 16640, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="linha_de_servico",
            name="projeto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="linha_de_servicos",
                to="empresa.projeto",
            ),
        ),
        migrations.AlterField(
            model_name="servico",
            name="projeto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="servicos",
                to="empresa.projeto",
            ),
        ),
    ]
