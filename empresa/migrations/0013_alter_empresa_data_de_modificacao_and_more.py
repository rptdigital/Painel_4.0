# Generated by Django 4.2.6 on 2023-11-27 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empresa", "0012_alter_empresa_data_de_modificacao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="data_de_modificacao",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 27, 22, 0, 6, 497604, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="proposta",
            name="data_de_aprovacao",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 27, 22, 0, 6, 497604, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="proposta",
            name="data_de_envio",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 27, 22, 0, 6, 497604, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="proposta",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 27, 22, 0, 6, 497604, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]