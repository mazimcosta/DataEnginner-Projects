# Pipeline Incremental de Vendas

Pipeline de Engenharia de Dados desenvolvido em Python para processar vendas de uma farmácia, validar registros, carregar dados no PostgreSQL e construir camadas analíticas seguindo a arquitetura Bronze, Silver e Gold.

O projeto utiliza processamento incremental com cursor e tabela de controle. Dessa forma, apenas registros ainda não processados são enviados para o banco.

---

## Objetivo

Construir um pipeline de dados capaz de:

- extrair dados de um arquivo CSV;
- validar os registros com Pydantic;
- separar registros válidos e inválidos;
- carregar apenas registros novos;
- executar UPSERT nas camadas Bronze e Silver;
- reconstruir as tabelas Gold;
- armazenar o último ID processado;
- evitar duplicação em reexecuções;
- registrar o fluxo e as falhas em logs.

---

## Tecnologias

- Python
- Pandas
- Pydantic
- PostgreSQL
- psycopg2
- SQL
- pytest
- GitHub Actions
- Git e GitHub

---

## Arquitetura

O pipeline foi dividido em módulos com responsabilidades específicas:

```text
pipeline_incremental/
│
├── config/
│   └── settings.py
│
├── data/
│   ├── input/
│   │   └── farmacia_1.csv
│   └── output/
│       ├── registros_validos.csv
│       └── registros_invalidos.csv
│
├── logs/
│   └── pipeline.log
│
├── sql/
│   ├── criar_tabelas.sql
│   ├── limpar_tabelas.sql
│   └── carregar_tabelas.sql
│
├── src/
│   ├── database.py
│   ├── extractor.py
│   ├── loader.py
│   ├── logger.py
│   ├── pipeline.py
│   ├── pipeline_control.py
│   ├── schema.py
│   └── sql_executor.py
│
├── tests/
│   ├── test_extractor.py
│   ├── test_logger.py
│   └── test_schema.py
│
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md