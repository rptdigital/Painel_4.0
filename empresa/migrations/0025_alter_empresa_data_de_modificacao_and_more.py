# Generated by Django 4.2.6 on 2023-12-04 16:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0024_statusprojeto_alter_empresa_data_de_modificacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='data_de_modificacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 16, 35, 39, 297115, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='status_projeto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projetos', to='empresa.statusprojeto'),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='data_de_aprovacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 16, 35, 39, 297115, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='data_de_envio',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 16, 35, 39, 297115, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 16, 35, 39, 297115, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='statusprojeto',
            name='nome',
            field=models.CharField(default='Não iniciado', max_length=200),
        ),
    ]
