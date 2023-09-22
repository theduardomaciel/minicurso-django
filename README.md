# Minicurso: Criação e manutenção de APIs REST usando Django e Django REST Framework

## 👩‍🎓 Sobre o minicurso
O minicurso que culminou no desenvolvimento deste projeto foi desenvolvido e ministrado pelos seguintes alunos do Instituto de Computação (IC) da Universidade Federal de Alagoas, durante a [Semana da Computação (SECOMP)](https://www.instagram.com/secomp.ufal/):
-   [ ] Paulo Victor
-   [ ] Iasmin Borba

<br />

## 💻 Como rodar o projeto

> [!IMPORTANT]  
> **Requisitos**: [Python](https://www.python.org/downloads/) instalado na máquina

<br />

#### Inicialização do projeto
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

#### Instalação, configuração e implementação do Django REST Framework

1. Para o desenvolvimento da API REST, começamos instalando o `Django REST Framework` com o seguinte comando:
```
pip install djangorestframework
```

2. Abrimos o arquivo `settings.py` localizado na raiz do projeto, e adicionamos na lista `INSTALLED_APPS` a seguinte linha: `rest_framework`

3. Caso seja desejável adicionar a autenticação padrão do Django, basta adicionar, no arquivo `urls.py` localizado na raiz do projeto, a seguinte linha à lista de **urlpatterns**: `path('api-auth/', include('rest_framework.urls'))`

4. Antes de criar as URLs, é necessário adicionar um **Serializer** para cada modelo. O arquivo `serializers.py` que deve ser criado dentro da pasta da **app** desejada (no nosso exemplo, `escola`), e neste arquivo que serão adicionados os **Serializers**.

5. Além dos **Serializers**, é necessário adicionar **Views**, classes que contém os métodos de CRUD de um determinado model, para cada **Model**.

> [!NOTE]  
> Além dos verbos HTTP padrões que compõem o CRUD (Create, Read, Update, Delete), é possível criar as próprias **Actions**, a fim de mais personalização.

6. Agora definindo as URLs, criamos um arquivo `urls.py` dentro da nossa app. Após realizar as importações corretamente (disponíveis no material de apoio), precisamos linkar as rotas desta aplicação ao projeto principal. <br />
   Para isso, seguimos para o urls.py na pasta de configuração do projeto. Nesse arquivo, importamos os routers definidos na app (e em todas as outras) e adicionamo-nos à lista `urlpatterns`.

<br />

### Observações
    1. Caso o sistema Linux apresente a configuração de idioma do teclado incorreta no Laboratório, utilize o comando: `setxkbmap br` no terminal
    2. Para instalar as dependências em um projeto já iniciado, utilize: `pip install -r requirements.txt`
	3. Definimos e importamos as URLs de forma individual por app para melhor organização, visto que as URLs de nossa app `escola` poderiam ter sido inseridas diretamente no arquivo `urls.py` da pasta de configurações do projeto._
