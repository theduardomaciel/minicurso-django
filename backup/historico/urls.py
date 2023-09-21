from rest_framework import routers
from .views import *

routerHistorico = routers.DefaultRouter()
routerHistorico.register("cidades", CidadeView)
routerHistorico.register("ufs", UfView)
