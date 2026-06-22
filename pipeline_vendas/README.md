# Pipeline V3 - Validação de Schema e Qualidade de Dados

## Visão Geral

Este projeto implementa um pipeline ETL simplificado para processamento de vendas utilizando Python puro.

O objetivo é simular problemas comuns encontrados em ambientes de Engenharia de Dados, aplicando validações estruturais (Schema Validation), validações de qualidade dos dados (Data Quality) e geração de relatórios operacionais.

---

## Objetivos

* Ler dados de vendas a partir de um arquivo CSV.
* Validar a estrutura esperada do arquivo.
* Validar a qualidade dos registros.
* Separar registros válidos e inválidos.
* Calcular métricas de negócio.
* Gerar arquivos de saída para consumo posterior.

---

## Arquitetura

```text
input/vendas.csv
        │
        ▼
extract.py
        │
        ▼
schema.py
        │
        ▼
transform.py
        │
        ▼
load.py
        │
        ▼
output/
├── vendas_validas.csv
└── relatorio.json
```

---

## Estrutura do Projeto

```text
pipeline_vendas/
│
├── input/
│   └── vendas.csv
│
├── output/
│   ├── vendas_validas.csv
│   └── relatorio.json
│
├── extract.py
├── schema.py
├── transform.py
├── load.py
├── main.py
└── README.md
```

---

## Responsabilidades dos Módulos

### extract.py

Responsável pela extração dos dados.

Funções:

* Leitura do arquivo CSV.
* Extração das colunas do arquivo.
* Tratamento de arquivo inexistente.

Retorno:

```python
dados_brutos, colunas_arquivo
```

---

### schema.py

Responsável pela validação estrutural.

Valida se o arquivo possui todas as colunas obrigatórias.

Colunas esperadas:

```python
[
    "produto",
    "preco",
    "quantidade",
    "categoria"
]
```

Caso alguma coluna esteja ausente:

```python
raise ValueError(...)
```

---

### transform.py

Responsável pelas regras de negócio.

Valida:

* Produto vazio.
* Preço vazio.
* Preço inválido.
* Preço menor ou igual a zero.
* Quantidade vazia.
* Quantidade inválida.
* Quantidade menor ou igual a zero.
* Categoria vazia.

Também calcula:

```text
faturamento = preco * quantidade
```

e gera:

* Lista de vendas válidas.
* Lista de vendas inválidas.
* Relatório consolidado.

---

### load.py

Responsável pela persistência.

Gera:

#### vendas_validas.csv

Contém apenas registros aprovados.

#### relatorio.json

Contém métricas do processamento.

Exemplo:

```json
{
  "validas": 10,
  "invalidas": 10,
  "erros": {
    "produto_vazio": 2,
    "preco_invalido": 1
  },
  "faturamento_total": 13462.0
}
```

---

### main.py

Responsável pela orquestração do pipeline.

Fluxo:

```text
Extração
↓
Validação de Schema
↓
Transformação
↓
Carga
```

Também realiza tratamento de exceções:

```python
FileNotFoundError
ValueError
```

---

## Regras de Qualidade de Dados

Um registro é considerado inválido quando:

* Produto está vazio.
* Preço está vazio.
* Preço não é numérico.
* Preço é menor ou igual a zero.
* Quantidade está vazia.
* Quantidade não é numérica.
* Quantidade é menor ou igual a zero.
* Categoria está vazia.

---

## Tecnologias Utilizadas

* Python 3
* csv
* json

---

## Conceitos Aplicados

* ETL
* Data Quality
* Schema Validation
* Tratamento de Exceções
* Arquitetura em Camadas
* Separação de Responsabilidades
* Geração de Relatórios
* Engenharia de Dados Fundamental

---

## Aprendizados

Durante a construção deste pipeline foram praticados:

* Leitura e escrita de arquivos CSV.
* Manipulação de dicionários.
* Estruturação de pipelines ETL.
* Validação estrutural de dados.
* Validação de regras de negócio.
* Tratamento de erros operacionais.
* Organização de projetos Python.
* Transferência de conceitos de APIs para pipelines de dados.

---

## Status

Projeto concluído com sucesso.

Funcionalidades implementadas:

* Extração de dados.
* Validação de schema.
* Validação de qualidade.
* Separação de registros válidos e inválidos.
* Geração de métricas.
* Exportação de CSV.
* Exportação de JSON.
* Tratamento de exceções.
* Documentação do pipeline.
