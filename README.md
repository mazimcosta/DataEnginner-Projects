# Projetos Data Engineer

Repositório dedicado ao desenvolvimento de projetos práticos de Engenharia de Dados utilizando Python, SQL e ferramentas do ecossistema de dados.

## Objetivo

Este repositório documenta minha evolução na área de Engenharia de Dados por meio da construção de projetos práticos focados em:

* Manipulação e processamento de dados
* Pipelines ETL
* SQL e modelagem de dados
* Bancos de dados relacionais
* Boas práticas de engenharia de software
* Tratamento e validação de dados
* Arquitetura de aplicações de dados

---

## Tecnologias Utilizadas

### Linguagens

* Python
* SQL

### Bibliotecas Nativas

* csv
* json

### Ferramentas

* Git
* GitHub
* SQLite
* PostgreSQL (em andamento)

---

## Estrutura do Repositório

```text
projetos-data-engineer/

├── pipeline-v1/
├── pipeline-v2/
├── pipeline-v3/
├── docs/
└── README.md
```

---

## Projetos

### Pipeline ETL V1

Primeira implementação do processo ETL.

Conceitos praticados:

* Extract
* Transform
* Load
* Leitura de arquivos CSV
* Manipulação de listas e dicionários
* Organização básica de código

---

### Pipeline ETL V2

Pipeline ETL completo com validação de dados e geração de relatórios.

Funcionalidades:

* Leitura de CSV utilizando DictReader
* Escrita de CSV utilizando DictWriter
* Geração de relatórios JSON
* Validação de dados
* Tratamento de exceções
* Separação entre registros válidos e inválidos

Validações implementadas:

* Nome vazio
* Idade vazia
* Idade inválida
* Idade negativa
* Gênero vazio
* Gênero inválido

Arquitetura:

```text
extract.py
schema.py
transform.py
load.py
main.py
```

Testes realizados:

* Arquivo vazio
* Coluna obrigatória ausente
* Arquivo sem cabeçalho
* Caminho inválido
* Registros inconsistentes

---

### Pipeline ETL V3

Projeto em desenvolvimento.

Objetivos:

* Processamento de vendas
* Validação de schema
* Cálculo de faturamento
* Relatórios de auditoria
* Consolidação dos conceitos de ETL

---

## Principais Aprendizados

Durante os projetos desenvolvidos foram praticados conceitos fundamentais de Engenharia de Dados:

* Separação de responsabilidades
* Validação de schema
* Qualidade de dados
* Tratamento de erros
* Processamento de arquivos
* Estruturas de dados em Python
* Pensamento orientado a pipelines
* Transferência de conhecimento entre domínios de negócio

---

## Roadmap Atual

Concluído:

* Python Básico
* Estruturas de Dados
* Programação Orientada a Objetos
* SQL Intermediário
* ETL V1
* ETL V2

Próximos passos:

* ETL V3
* PostgreSQL
* Modelagem de Dados
* Consultas Analíticas
* Engenharia de Dados

---

## Autor

Desenvolvedor Python e estudante de Engenharia de Dados, construindo projetos práticos para consolidar conhecimentos em backend, bancos de dados e pipelines de processamento de dados.
