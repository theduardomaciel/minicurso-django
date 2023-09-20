from django.db import models

# Create your models here.
class Postagem(models.Model):
    id_postagem = models.AutoField(primary_key=True)
    titulo = models.CharField(null=True, blank=True, max_length=100)
    texto = models.TextField()
    data = models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-data', 'titulo']
        db_table='qualquer_coisa'
        unique_together=['titulo', 'data'] # nao pode ter uma postagem com o mesmo titulo na mesma data

class Comentario(models.Model):
    id_postagem = models.AutoField(primary_key=True)
    texto = models.TextField()
    data = models.DateField(auto_now_add=True)

    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

# no shell (aberto por `python manage.py shell`): from blog.models import Postagem