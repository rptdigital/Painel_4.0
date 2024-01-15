# Generated by Django 4.2.6 on 2023-11-29 20:24

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("empresa", "0013_alter_empresa_data_de_modificacao_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comb_servico",
            name="servico",
        ),
        migrations.AlterField(
            model_name="comb_servico",
            name="proposta",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="modulos",
                to="empresa.proposta",
            ),
        ),
        migrations.AlterField(
            model_name="contato",
            name="celular",
            field=models.CharField(
                max_length=11,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_cell_number",
                        message="O número de celular deve conter exatamente 11 dígitos.",
                        regex="^\\d{11}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="contato",
            name="telefone",
            field=models.CharField(
                max_length=11,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_tell_number",
                        message="O número do telefone deve conter exatamente 8 dígitos.",
                        regex="^\\d{8}$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="empresa",
            name="data_de_modificacao",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 29, 20, 24, 17, 703349, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="endereco",
            name="complemento",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="proposta",
            name="data_de_aprovacao",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 29, 20, 24, 17, 703349, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="proposta",
            name="data_de_envio",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 29, 20, 24, 17, 703349, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="proposta",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 29, 20, 24, 17, 703349, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="proposta",
            name="estagio",
            field=models.CharField(
                choices=[
                    ("Pendente", "Pendente"),
                    ("Média Probabilidade", "Média Longo"),
                    ("Alta Probabilidade", "Alta Probabilidade"),
                    ("Enviada", "Enviada"),
                    ("Aprovado", "Aprovado"),
                    ("Declinada", "Declinada"),
                    ("Cancelada", "Cancelada"),
                    ("Recusamos", "Recusamos"),
                ],
                max_length=100,
            ),
        ),
        migrations.CreateModel(
            name="Modulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=150)),
                (
                    "servico",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="modulo",
                        to="empresa.servico",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="comb_servico",
            name="modulo",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="combinacoes_servicos",
                to="empresa.modulo",
            ),
        ),
    ]