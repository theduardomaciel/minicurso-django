from django.db import models

class Alunos(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=8, unique=True)
    matricula = models.CharField(max_length=8, unique=True)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=255, unique=True)

    class Meta:
        db_table = "alunos"
        ordering = ["id_aluno"]

class Professores(models.Model):
    id_professor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=8, unique=True)
    codigo = models.CharField(max_length=8)
    email = models.EmailField(max_length=255, unique=True)
    telefone = models.CharField(max_length=11)

    class Meta:
        db_table = "professores"
        ordering = ["id_professor"]

class Disciplinas(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    id_professor = models.ForeignKey(Professores, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=7)
    carga_horaria = models.IntegerField()
    ementa = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "disciplinas"
        ordering = ["id_disciplina"]

class DisciplinaAluno(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = "disciplina_aluno"
        ordering = ["id_matricula"]

class Frequencia(models.Model):
    id_frequencia = models.AutoField(primary_key=True)
    id_materia = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    dia = models.DateField()

    class Meta:
        db_table = "frequencia"
        ordering = ["id_frequencia"]

class FrequenciaAluno(models.Model):
    id = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    id_frequencia = models.ForeignKey(Frequencia, on_delete=models.CASCADE)
    presenca = models.BooleanField(default=True)

    class Meta:
        db_table = "frequencia_aluno"
        ordering = ["id"]

class PlanoAula(models.Model):
    id_plano_aula = models.AutoField(primary_key=True)
    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    tema_aula = models.CharField(max_length=255)
    conteudo = models.TextField()

    metodos = (
        ('Teórica', 'Teórica'),
        ('Prática', 'Prática')
    )

    metodo = models.CharField(max_length=7, choices=metodos)
    dia = models.DateField()

    class Meta:
        db_table = "plano_aula"
        ordering = ["id_plano_aula"]

class Atividades(models.Model):
    id_atividade = models.AutoField(primary_key=True)
    atividade = models.TextField()
    tipo = models.CharField(max_length=50)
    data_postagem = models.DateField(auto_now_add=True)
    data_entrega = models.DateField()

    id_disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    id_plano_aula = models.ForeignKey(PlanoAula, on_delete=models.CASCADE)

    class Meta:
        db_table = "atividades"
        ordering = ["id_atividade"]

class AtividadeAluno(models.Model):
    id = models.AutoField(primary_key=True)
    id_atividade = models.ForeignKey(Atividades, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)

    class Meta:
        db_table = "atividade_aluno"
        ordering = ["id"]