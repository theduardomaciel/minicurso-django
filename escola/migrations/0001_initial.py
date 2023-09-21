# Generated by Django 4.2.5 on 2023-09-21 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alunos",
            fields=[
                ("id_aluno", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=11, unique=True)),
                ("rg", models.CharField(max_length=8, unique=True)),
                ("matricula", models.CharField(max_length=8, unique=True)),
                ("telefone", models.CharField(max_length=11)),
                ("email", models.EmailField(max_length=255, unique=True)),
            ],
            options={
                "db_table": "alunos",
                "ordering": ["id_aluno"],
            },
        ),
        migrations.CreateModel(
            name="Disciplinas",
            fields=[
                ("id_disciplina", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=255)),
                ("codigo", models.CharField(max_length=7)),
                ("carga_horaria", models.IntegerField()),
                ("ementa", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "disciplinas",
                "ordering": ["id_disciplina"],
            },
        ),
        migrations.CreateModel(
            name="Frequencia",
            fields=[
                ("id_frequencia", models.AutoField(primary_key=True, serialize=False)),
                ("dia", models.DateField()),
                (
                    "id_materia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="escola.disciplinas",
                    ),
                ),
            ],
            options={
                "db_table": "frequencia",
                "ordering": ["id_frequencia"],
            },
        ),
        migrations.CreateModel(
            name="Professores",
            fields=[
                ("id_professor", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=11, unique=True)),
                ("rg", models.CharField(max_length=8, unique=True)),
                ("codigo", models.CharField(max_length=8)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("telefone", models.CharField(max_length=11)),
            ],
            options={
                "db_table": "professores",
                "ordering": ["id_professor"],
            },
        ),
        migrations.CreateModel(
            name="PlanoAula",
            fields=[
                ("id_plano_aula", models.AutoField(primary_key=True, serialize=False)),
                ("tema_aula", models.CharField(max_length=255)),
                ("conteudo", models.TextField()),
                (
                    "metodo",
                    models.CharField(
                        choices=[("Teórica", "Teórica"), ("Prática", "Prática")],
                        max_length=7,
                    ),
                ),
                ("dia", models.DateField()),
                (
                    "id_disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="escola.disciplinas",
                    ),
                ),
            ],
            options={
                "db_table": "plano_aula",
                "ordering": ["id_plano_aula"],
            },
        ),
        migrations.CreateModel(
            name="FrequenciaAluno",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("presenca", models.BooleanField(default=True)),
                (
                    "id_aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="escola.alunos"
                    ),
                ),
                (
                    "id_frequencia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="escola.frequencia",
                    ),
                ),
            ],
            options={
                "db_table": "frequencia_aluno",
                "ordering": ["id"],
            },
        ),
        migrations.AddField(
            model_name="disciplinas",
            name="id_professor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="escola.professores"
            ),
        ),
        migrations.CreateModel(
            name="DisciplinaAluno",
            fields=[
                ("id_matricula", models.AutoField(primary_key=True, serialize=False)),
                (
                    "nota",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "id_aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="escola.alunos"
                    ),
                ),
                (
                    "id_disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="escola.disciplinas",
                    ),
                ),
            ],
            options={
                "db_table": "disciplina_aluno",
                "ordering": ["id_matricula"],
            },
        ),
        migrations.CreateModel(
            name="Atividades",
            fields=[
                ("id_atividade", models.AutoField(primary_key=True, serialize=False)),
                ("atividate", models.TextField()),
                ("tipo", models.CharField(max_length=50)),
                ("data_postagem", models.DateField(auto_now_add=True)),
                ("data_entrega", models.DateField()),
                (
                    "id_disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="escola.disciplinas",
                    ),
                ),
                (
                    "id_plano_aula",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="escola.planoaula",
                    ),
                ),
            ],
            options={
                "db_table": "atividades",
                "ordering": ["id_atividade"],
            },
        ),
        migrations.CreateModel(
            name="AtividadeAluno",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "id_aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="escola.alunos"
                    ),
                ),
                (
                    "id_atividade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="escola.atividades",
                    ),
                ),
            ],
            options={
                "db_table": "atividade_aluno",
                "ordering": ["id"],
            },
        ),
    ]
