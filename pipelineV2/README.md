# Pipeline ETL V2 - Validação e Tratamento de Dados

## Descrição

O Pipeline ETL V2 foi desenvolvido com o objetivo de processar dados de clientes armazenados em arquivos CSV, aplicando validações, separando registros válidos e inválidos e gerando relatórios para auditoria.

Este projeto foi criado para consolidar conceitos fundamentais de Engenharia de Dados, como ETL, qualidade de dados, tratamento de erros e separação de responsabilidades.

---

## Objetivo

Ler um arquivo CSV contendo informações de clientes, validar os dados, gerar um novo arquivo contendo apenas registros válidos e produzir um relatório com os erros encontrados durante o processamento.

---

## Fluxo do Pipeline

```text
Extract
↓
Validate Schema
↓
Transform
↓
Load
```

---

## Estrutura do Projeto

```text
pipeline_v2/

├── input/
│   └── clientes.csv
│
├── output/
│   ├── clientes_validos.csv
│   └── relatorio.json
│
├── extract.py
├── schema.py
├── transform.py
├── load.py
└── main.py
```

---

## Responsabilidades dos Módulos

### extract.py

Responsável por:

* Ler o arquivo CSV
* Extrair os dados para memória
* Obter as colunas presentes no arquivo

---

### schema.py

Responsável por:

* Validar a estrutura do arquivo
* Garantir a existência das colunas obrigatórias

Schema esperado:

```text
nome
idade
genero
```

Caso alguma coluna esteja ausente:

```text
ValueError
```

é lançado e o processamento é interrompido.

---

### transform.py

Responsável por:

* Validar os registros
* Separar clientes válidos e inválidos
* Construir o relatório de processamento

Validações implementadas:

#### Nome

* Não pode estar vazio
* Não pode conter apenas espaços
* Deve conter apenas caracteres alfabéticos

#### Idade

* Não pode estar vazia
* Deve ser numérica
* Deve ser maior ou igual a zero

#### Gênero

* Não pode estar vazio
* Não pode conter apenas espaços
* Deve pertencer aos valores permitidos

---

### load.py

Responsável por:

* Gerar o arquivo CSV limpo
* Gerar o relatório JSON

---

### main.py

Responsável por:

* Orquestrar todo o fluxo do pipeline
* Controlar o tratamento de erros

---

## Entradas

Exemplo de arquivo de entrada:

```csv
nome,idade,genero
Joao,25,M
Maria,30,F
Carlos,-5,M
Ana,,F
```

---

## Saídas

### clientes_validos.csv

Contém apenas registros aprovados nas validações.

Exemplo:

```csv
nome,idade,genero
Joao,25,M
Maria,30,F
```

---

### relatorio.json

Contém métricas e informações de auditoria.

Exemplo:

```json
{
    "total_registros": 4,
    "validos": 2,
    "invalidos": 2,
    "erros": {
        "idade_negativa": 1,
        "idade_vazia": 1
    }
}
```

---

## Tratamento de Erros

O pipeline foi testado contra diversos cenários de falha:

### Arquivo inexistente

```text
FileNotFoundError
```

Tratado de forma controlada.

---

### Arquivo vazio

Resultado esperado:

```text
0 válidos
0 inválidos
```

---

### Coluna obrigatória ausente

Exemplo:

```csv
nome,idade
```

Resultado:

```text
Erro de schema
```

---

### Arquivo sem cabeçalho

Detectado durante a validação de schema.

---

## Conceitos Aplicados

* ETL (Extract, Transform, Load)
* Validação de Schema
* Qualidade de Dados
* Tratamento de Exceções
* Manipulação de CSV
* Manipulação de JSON
* Dicionários
* Listas
* Funções
* Separação de Responsabilidades
* Arquitetura Modular

---

## Tecnologias Utilizadas

* Python 3
* csv
* json

---

## Aprendizados

Durante o desenvolvimento deste projeto foram consolidados conhecimentos em:

* Processamento de arquivos
* Validação de dados
* Tratamento de erros
* Auditoria de registros inválidos
* Construção de pipelines resilientes
* Pensamento orientado a Engenharia de Dados

---

## Próxima Evolução

Pipeline ETL V3:

* Novo domínio de negócio
* Cálculo de métricas
* Novas validações
* Consolidação do padrão ETL
* Transfer Learning entre projetos
