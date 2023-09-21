from rest_framework import serializers
from .models import *


class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = "__all__"
