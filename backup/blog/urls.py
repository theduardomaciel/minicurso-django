from rest_framework import routers
from .views import *

routerBlog = routers.DefaultRouter()
routerBlog.register(r"postagem", PostagemView)
