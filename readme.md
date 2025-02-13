# Documentação da API - Plano de Estudos

## Visão Geral
Esta API foi desenvolvida para ajudar usuários a criarem um plano de estudos baseado em suas horas disponíveis e nas matérias que desejam estudar. A distribuição do tempo de estudo é feita considerando a dificuldade, peso e número de tópicos de cada matéria.

## Link do Repositório
O código-fonte está disponível no GitHub:
[https://github.com/Nexus-Dados/nexus-calendario-estudo-enem](https://github.com/Nexus-Dados/nexus-calendario-estudo-enem)

## Acessando a API
Se você deseja apenas utilizar a API, acesse:
[https://nexus-calendario-estudo-enem.onrender.com](https://nexus-calendario-estudo-enem.onrender.com)

A documentação interativa gerada pelo FastAPI está disponível em:
[https://nexus-calendario-estudo-enem.onrender.com/docs](https://nexus-calendario-estudo-enem.onrender.com/docs)

## Instalação para Contribuição
Caso você queira contribuir com o projeto, siga os passos abaixo:

### 1. Configurar Python 3.11
Certifique-se de que o `pyenv` está instalado e configure a versão correta do Python:

```sh
pyenv install 3.11
pyenv local 3.11
```

### 2. Clonar o Repositório

```sh
git clone https://github.com/Nexus-Dados/nexus-calendario-estudo-enem.git
cd nexus-calendario-estudo-enem
```

### 3. Criar e Ativar um Ambiente Virtual

```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 4. Instalar Dependências

```sh
pip install -r requirements.txt
```

### 5. Executar a API Localmente

```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

A API estará acessível em: [http://localhost:8000](http://localhost:8000)

## Considerações Finais
Este projeto pode ser expandido para incluir funcionalidades como salvar as recomendações em um banco de dados ou integrar com calendários. Contribuições são bem-vindas!

