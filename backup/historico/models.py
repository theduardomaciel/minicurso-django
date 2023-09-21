from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(max_length=30, null=True, blank=True)
    first_name = models.TextField(max_length=30, null=True, blank=True)
    last_name = models.TextField(max_length=30, null=True, blank=True)


class Conta(models.Model):
    id_conta = models.AutoField(primary_key=True)

    tipos_conta = (("Poupança", "Poupança"), ("Corrente", "Corrente"))
    tipo_conta = models.CharField(max_length=30, choices=tipos_conta)

    id_banco = models.IntegerField()

    bancos = (
        ("Banco 1", "Banco 1"),
        ("Banco 2", "Banco 2"),
        ("Banco 3", "Banco 3"),
        ("Banco 4", "Banco 4"),
    )
    banco = models.CharField(max_length=7, choices=bancos)

    conta = models.IntegerField()
    agencia = models.IntegerField()
    operacao = models.IntegerField()


class UnidadeFederativa(models.Model):
    id_uf = models.AutoField(primary_key=True)
    nome_uf = models.CharField(max_length=30)
    sigla_uf = models.CharField(max_length=2)

    class Meta:
        ordering = ["nome_uf"]
        db_table = "Ufs"
        unique_together = ["nome_uf", "sigla_uf"]


class Cidade(models.Model):
    id_cidade = models.AutoField(primary_key=True)

    nome_cidade = models.CharField(max_length=50)
    id_uf = models.ForeignKey(UnidadeFederativa, on_delete=models.CASCADE)

    class Meta:
        ordering = ["nome_cidade"]
        db_table = "Cidades"
        unique_together = ["nome_cidade", "id_uf"]


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)

    id_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=8)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=80)
    complemento = models.CharField(max_length=60, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "Endereços"


class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)

    vinculos = (("Vinculo 1", "Vinculo 1"), ("Vinculo 2", "Vinculo 2"))
    vinculo = models.CharField(max_length=9, choices=vinculos)

    auth_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_conta = models.ForeignKey(Conta, on_delete=models.CASCADE)

    cpf = models.IntegerField()
    nome = models.TextField(max_length=200)
    telefone = models.TextField(max_length=16)
    email = models.EmailField()

    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


class Ocorrencia(models.Model):
    id_ocorrencia = models.AutoField(primary_key=True)
    data = models.DateField(auto_now_add=True)
    realizada = models.CharField(max_length=1)
    ocorrencia = models.TextField()

    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
