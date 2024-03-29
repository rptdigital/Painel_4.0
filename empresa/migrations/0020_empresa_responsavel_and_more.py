# Generated by Django 4.2.6 on 2023-11-30 22:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0019_remove_contato_cidade_contato_endereco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresas', to='empresa.responsavel'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='data_de_modificacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 22, 29, 43, 397876, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='data_de_aprovacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 22, 29, 43, 397876, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='data_de_envio',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 22, 29, 43, 397876, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 22, 29, 43, 397876, tzinfo=datetime.timezone.utc)),
        ),
    ]
