# API Lambda com Chalice

Este README fornece um guia completo sobre como criar e implantar uma API Lambda na AWS utilizando a biblioteca Chalice. O guia abrange desde a criação de um ambiente virtual até o deploy da API.

## Descrição

Este guia irá orientá-lo através dos passos necessários para desenvolver uma API Lambda utilizando Chalice, incluindo a configuração do ambiente de desenvolvimento, instalação de dependências, criação do código da API e deploy no AWS Lambda.

## Pré-requisitos

Antes de começar, certifique-se de que tem o seguinte configurado em seu sistema:

- Sistema operacional Linux (Ubuntu ou Debian recomendado)
- Python instalado
- Conta AWS com acesso à AWS CLI configurado

## Passo a Passo

### 1. Criação de Ambiente Virtual (venv)

Primeiro, crie e ative um ambiente virtual para isolar as dependências do projeto:

Para a crialção:

    python3 -m venv venv
Para a ativação:

    source venv/bin/activate

### 2. Instalação das Bibliotecas Chalice e Pytest

Instale as bibliotecas necessárias dentro do ambiente virtual:

    pip install Chalice pytest

### 3. Configuração da AWS CLI

Se ainda não tiver a AWS CLI instalada, faça-o e configure-a:

    sudo apt install awscli

Configuração awscli:

    aws configure

### 4. Criação do Projeto Chalice

Inicialize um novo projeto Chalice:

    Chalice new-project

Isto cria uma estrutura básica de projeto em um diretório chamado `app`.

### 5. Edição do Código da API (arquivo app.py)

Abra o arquivo `app.py` e desenvolva a lógica de sua API. Consulte a documentação da Chalice para mais detalhes sobre como definir endpoints e outros aspectos da API.

### 6. Execução de Testes Unitários

Garanta a qualidade do código executando os testes unitários:

    pytest ./tests/test_app.py

### 7. Deploy da API na AWS

Faça o deploy de sua API na AWS:

    Chalice deploy

Anote o URL gerado após o deploy para acessar sua API.

## Recursos Adicionais

- Documentação Chalice: [https://aws.github.io/chalice/main.html](https://aws.github.io/chalice/main.html)
- Documentação Pytest: [https://docs.pytest.org/en/7.1.x/contents.html](https://docs.pytest.org/en/7.1.x/contents.html)
- Documentação AWS CLI: [https://docs.aws.amazon.com/cli/](https://docs.aws.amazon.com/cli/)

## Conclusão

Este guia oferece uma base sólida para o desenvolvimento de sua API Lambda usando Chalice.
