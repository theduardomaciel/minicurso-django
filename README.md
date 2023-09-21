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

5. Iniciamos o projeto Django com um dado nome, no exemplo abaixo escolhemos `minicurso`
```
django-admin startproject minicurso .
```

6. Criamos um novo app com um dado nome no projeto, para melhor organização. No exemplo escolhemos `blog`
```
python manage.py startapp blog
```
> Observações: 
    1. Caso o sistema Linux apresente a configuração de idioma do teclado incorreta no Laboratório, utilize o comando: `setxkbmap br` no terminal
    2. Para instalar as dependências em um projeto já iniciado, utilize: `pip install -r requirements.txt`