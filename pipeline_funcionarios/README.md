# Pipeline de Funcionários

## Objetivo

Pipeline ETL desenvolvido em Python para processar dados de funcionários a partir de um arquivo CSV.

O pipeline realiza:

* Extração dos dados
* Validação de schema
* Validação de regras de negócio
* Classificação por faixa salarial
* Geração de relatórios
* Exportação de funcionários válidos e inválidos

---

## Estrutura do Projeto

```text
projeto/
│
├── input/
│   └── funcionários.csv
│
├── output/
│   ├── funcionarios_validos.csv
│   ├── funcionarios_invalidos.csv
│   └── relatorio.json
│
├── extract.py
├── schema.py
├── transform.py
├── load.py
├── main.py
│
└── README.md
```

---

## Fluxo do Pipeline

```text
CSV
 ↓
Extract
 ↓
Schema Validation
 ↓
Transform
 ↓
Load
```

### 1. Extract

Responsável por ler o arquivo CSV.

Arquivo:

```text
extract.py
```

Função:

```python
extrair_dados()
```

Retorna:

* dados do arquivo
* colunas encontradas

---

### 2. Schema Validation

Responsável por validar a estrutura do arquivo.

Arquivo:

```text
schema.py
```

Função:

```python
validar_schema()
```

Valida:

* existência de cabeçalho
* colunas obrigatórias

Colunas obrigatórias:

```text
nome
email
salario
departamento
```

---

### 3. Transform

Responsável pelas regras de negócio.

Arquivo:

```text
transform.py
```

Função:

```python
processar_dados()
```

Valida:

* nome vazio
* email vazio
* email inválido
* salário vazio
* salário inválido
* salário menor ou igual a zero
* departamento vazio

Classificação salarial:

```text
< 4000      → junior
4000-9000   → pleno
> 9000      → senior
```

Também calcula:

* quantidade de válidos
* quantidade de inválidos
* folha salarial total
* média salarial

---

### 4. Load

Responsável pela geração dos arquivos de saída.

Arquivo:

```text
load.py
```

Arquivos gerados:

#### Funcionários válidos

```text
output/funcionarios_validos.csv
```

#### Funcionários inválidos

```text
output/funcionarios_invalidos.csv
```

Contém:

```text
nome
email
salario
departamento
erro
```

#### Relatório

```text
output/relatorio.json
```

Contém:

```json
{
    "validos": 0,
    "invalidos": 0,
    "erros": {},
    "folha_total": 0,
    "media_salarial": 0
}
```

---

## Como Executar

Executar:

```bash
python main.py
```

---

## Exemplo de Entrada

```csv
nome,email,salario,departamento
João,joao@email.com,5000,TI
Maria,maria@email.com,3000,RH
Pedro,,4500,Financeiro
```

---

## Exemplo de Saída

### Funcionários válidos

```csv
nome,email,salario,departamento,faixa_salarial
João,joao@email.com,5000,TI,pleno
Maria,maria@email.com,3000,RH,junior
```

### Funcionários inválidos

```csv
nome,email,salario,departamento,erro
Pedro,,4500,Financeiro,email_invalido
```

---

## Tecnologias Utilizadas

* Python 3
* csv
* json

---

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

* leitura de arquivos CSV
* manipulação de dicionários
* tratamento de exceções
* validação de dados
* organização em módulos
* separação de responsabilidades
* geração de relatórios
* persistência de dados inválidos para auditoria
* leitura de logs e identificação de erros

```
```
