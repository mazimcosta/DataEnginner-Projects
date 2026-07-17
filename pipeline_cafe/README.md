# ☕ Pipeline Café - Engenharia de Dados

Pipeline de Engenharia de Dados desenvolvido em Python utilizando a Arquitetura Medalhão (Bronze, Silver e Gold).

O projeto simula um cenário próximo ao mercado, implementando um pipeline incremental, validação de dados com Pydantic, transformação utilizando Pandas e carga em PostgreSQL.

---

# Arquitetura

```
CSV
 │
 ▼
Extractor
 │
 ▼
Transformer
 │
 ▼
Schema (Pydantic)
 │
 ▼
Bronze
 │
 ▼
Silver
 │
 ▼
Gold
```

---

# Tecnologias

- Python 3.13
- Pandas
- PostgreSQL
- Pydantic V2
- Psycopg
- Pytest
- SQL

---

# Funcionalidades

- Extração de dados CSV
- Limpeza e padronização
- Conversão segura de tipos
- Validação utilizando Pydantic
- Separação entre registros válidos e inválidos
- Registro detalhado de erros
- Controle de processamento incremental
- Carga em arquitetura Bronze / Silver / Gold
- Agregações analíticas utilizando SQL
- Testes unitários com Pytest
- Logging estruturado

---

# Estrutura do Projeto

```
pipeline_cafe/

│
├── config/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── logs/
│
├── sql/
│   ├── criar_tabelas.sql
│   ├── carregar_tabelas.sql
│   └── limpar_tabelas.sql
│
├── src/
│   ├── extractor.py
│   ├── transformer.py
│   ├── schema.py
│   ├── loader.py
│   ├── pipeline.py
│   ├── database.py
│   ├── pipeline_control.py
│   ├── logger.py
│   └── sql_executor.py
│
├── tests/
│
├── main.py
└── requirements.txt
```

---

# Camadas

## Bronze

Armazena os dados válidos praticamente no formato original, preservando o histórico de ingestão.

Contém:

- transacao_id
- id_incremental
- produto
- quantidade
- preço
- valor_total
- método_pagamento
- localidade
- data_transacao

---

## Silver

Camada responsável pela padronização dos dados.

Nesta etapa são realizadas transformações como:

- normalização dos textos
- tratamento de datas
- criação das colunas mês
- criação das colunas ano

---

## Gold

Camada analítica.

São geradas tabelas agregadas para consultas rápidas.

Exemplos:

- faturamento por produto
- vendas por produto
- faturamento por localidade
- faturamento por mês
- faturamento por ano

---

# Controle Incremental

O projeto implementa processamento incremental utilizando a tabela:

```
pipeline_controle
```

Ela armazena:

- nome do pipeline
- último id processado
- data da última execução

Isso evita reprocessamento desnecessário.

---

# Validação

A validação dos registros é realizada utilizando Pydantic.

Registros inválidos:

- não interrompem o pipeline
- são registrados em log
- são descartados antes da carga

---

# Testes

O projeto possui testes unitários utilizando Pytest para validar:

- transformação de textos
- conversão numérica
- tratamento de datas
- geração dos arquivos
- carga dos dados

Executar:

```bash
pytest
```

---

# Executando o Projeto

Instalar dependências

```bash
pip install -r requirements.txt
```

Criar tabelas

```bash
psql -f sql/criar_tabelas.sql
```

Executar pipeline

```bash
python main.py
```

---

# Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

- Engenharia de Dados
- Arquitetura Medalhão
- ETL
- Processamento Incremental
- SQL Analítico
- Validação de Dados
- Logging
- Testes Automatizados
- Organização em Camadas
- Clean Code

---

# Próximos Passos

- Docker
- Apache Airflow
- Parquet
- Particionamento
- Amazon S3
- Data Lake
- Dashboard em Power BI
- Orquestração de pipelines

---

# Autor

Francisco Mazim

- LinkedIn:
  https://www.linkedin.com/in/mazim-costa-699696301/

- GitHub:
  https://github.com/mazimcosta