from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.


class CidadeView(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


class UfView(viewsets.ModelViewSet):
    queryset = UnidadeFederativa.objects.all()
    serializer_class = CidadeSerializer
