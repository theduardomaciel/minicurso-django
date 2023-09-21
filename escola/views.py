from rest_framework import viewsets
from .models import *
from .serializers import *

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professores.objects.all()
    serializer_class = ProfessorSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplinas.objects.all()
    serializer_class = DisciplinaSerializer

class DisciplinaAlunoViewSet(viewsets.ModelViewSet):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class FrequenciaAlunoViewSet(viewsets.ModelViewSet):
    queryset = FrequenciaAluno.objects.all()
    serializer_class = FrequenciaAlunoSerializer

class PlanoAulaViewSet(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = PlanoAulaSerializer

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividades.objects.all()
    serializer_class = AtividadeSerializer

class AtividadeAlunoViewSet(viewsets.ModelViewSet):
    queryset = AtividadeAluno.objects.all()
    serializer_class = AtividadeAlunoSerializer