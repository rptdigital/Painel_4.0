# Generated by Django 4.2.6 on 2023-11-30 22:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0020_empresa_responsavel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='uf',
        ),
        migrations.AddField(
            model_name='empresa',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresas', to='empresa.cidade'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='data_de_modificacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 22, 45, 2, 223573, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='data_de_aprovacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 22, 45, 2, 223573, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='data_de_envio',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 22, 45, 2, 223573, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 30, 22, 45, 2, 223573, tzinfo=datetime.timezone.utc)),
        ),
    ]