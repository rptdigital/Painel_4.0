# Generated by Django 4.2.6 on 2023-10-26 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empresa", "0002_empresa_delete_filme"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="data_de_modificacao",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 26, 21, 24, 13, 332649, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
