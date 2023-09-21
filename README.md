# Minicurso: Criação e manutenção de APIs REST usando Django e Django REST Framework

## 💻 Como inicializar o projeto

> Requisitos: Python instalado na máquina

1. Criamos um ambiente virtual Python nomeado `env`, para não instalar pacotes desnecessários no Python global da máquina
```
python -m venv env
```

2. Ativamos o ambiente virtual (comando para o ambiente Linux)
```
source env/bin/activate
```

3. Instalamos o Django no ambiente virtual criado na pasta do projeto
```
python -m pip install Django
```

4. Criamos um arquivo `requirements.txt` contendo todas as dependências do projeto, para futuras instalações
```
pip freeze > requirements.txt
```

5. Iniciamos o projeto Django com um dado nome, no exemplo abaixo escolhemos `core`
```
django-admin startproject core .
```

6. Criamos um novo app com um dado nome no projeto, para melhor organização. No exemplo escolhemos `escola`
```
python manage.py startapp escola
```

7. Após adicionarmos os modelos, podemos criar e aplicar as migrações:
```
python manage.py makemigrations app
python manage.py migrate app
```

#### Django REST Framework

1. Começamos instalando o `Django REST Framework` com o seguinte comando:
```
pip install djangorestframework
```

2. Abrimos o arquivo `settings.py` localizado na raiz do projeto, e adicionamos na lista `INSTALLED_APPS` a seguinte linha: `rest_framework`

3. Caso seja desejável adicionar a autenticação padrão do Django, basta adicionar, no arquivo `urls.py` localizado na raiz do projeto, a seguinte linha à lista de **urlpatterns**: `path('api-auth/', include('rest_framework.urls'))`

4. Antes de criar as URLs, é necessário adicionar um **Serializer** para cada modelo. O arquivo `serializers.py` que deve ser criado dentro da pasta da **app** desejada (no nosso exemplo, `escola`), e neste arquivo que serão adicionados os **Serializers**.

5. Além dos **Serializers**, é necessário adicionar uma **View**, classe que contém os métodos de CRUD de um determinado model, para cada **Model**. 

> Observações: 
    1. Caso o sistema Linux apresente a configuração de idioma do teclado incorreta no Laboratório, utilize o comando: `setxkbmap br` no terminal
    2. Para instalar as dependências em um projeto já iniciado, utilize: `pip install -r requirements.txt`