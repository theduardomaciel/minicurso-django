from rest_framework import serializers
from .models import *


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = "__all__"


class UfSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeFederativa
        fields = "__all__"
