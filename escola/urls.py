from rest_framework import routers
from .views import *

routerEscola = routers.DefaultRouter()
routerEscola.register(r'alunos', AlunoViewSet)
routerEscola.register(r'professores', ProfessorViewSet)
routerEscola.register(r'disciplinas', DisciplinaViewSet)
routerEscola.register(r'disciplina_aluno', DisciplinaAlunoViewSet)
routerEscola.register(r'frequencia', FrequenciaViewSet)
routerEscola.register(r'frequencia_aluno', FrequenciaAlunoViewSet)
routerEscola.register(r'plano_aula', PlanoAulaViewSet)
routerEscola.register(r'atividades', AtividadeViewSet)
routerEscola.register(r'atividade_aluno', AtividadeAlunoViewSet)