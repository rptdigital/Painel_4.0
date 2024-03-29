# Generated by Django 4.2.6 on 2023-12-08 01:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0027_alter_empresa_data_de_modificacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='data_de_modificacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 1, 26, 9, 870185, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='data_de_aprovacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 1, 26, 9, 870185, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='data_de_envio',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 1, 26, 9, 870185, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 1, 26, 9, 870185, tzinfo=datetime.timezone.utc)),
        ),
    ]
