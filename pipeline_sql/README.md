# Pipeline SQL com Arquitetura Medalhão

## Sobre o projeto

Este projeto implementa um pipeline de dados utilizando Python, PostgreSQL e SQL, seguindo a Arquitetura Medalhão (Bronze, Silver e Gold).

O pipeline realiza a extração de um arquivo CSV contendo dados de vendas de um mercado, valida os registros utilizando Pydantic, carrega os dados para o PostgreSQL e gera camadas analíticas para consumo.

O objetivo do projeto é demonstrar a construção de um pipeline organizado, automatizado e preparado para evoluir para cargas robustas.

---

# Arquitetura

```
CSV
 │
 ▼
Extração
 │
 ▼
Validação (Pydantic)
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

# Camadas

## Bronze

Responsável por armazenar os dados válidos exatamente como foram recebidos após a validação estrutural.

Não existem agregações.

---

## Silver

Responsável pela aplicação das regras de negócio.

Transformações realizadas:

- apenas vendas com pagamento aprovado;
- quantidade maior que zero;
- preço unitário maior que zero;
- cálculo do valor bruto;
- cálculo do valor líquido.

---

## Gold

Camada destinada à análise de dados.

São geradas quatro tabelas analíticas:

- faturamento por categoria;
- faturamento por cliente;
- faturamento por cidade;
- faturamento por dia.

---

# Estrutura do projeto

```
pipeline_sql/

├── config/
│   └── settings.py
│
├── data/
│   ├── input/
│   └── output/
│
├── logs/
│   └── pipeline.log
│
├── sql/
│   ├── create_tables.sql
│   ├── clear_tables.sql
│   └── load_tables.sql
│
├── src/
│   ├── extractor.py
│   ├── loader.py
│   ├── logger.py
│   ├── pipeline.py
│   ├── schema.py
│   └── sql_executor.py
│
├── tests/
│
├── main.py
│
└── README.md
```

---

# Tecnologias utilizadas

- Python
- PostgreSQL
- SQL
- Pandas
- Pydantic
- Psycopg2
- Pytest

---

# Funcionalidades

- Extração de dados CSV
- Validação com Pydantic
- Separação de registros válidos e inválidos
- Criação automática das tabelas
- Limpeza automática das tabelas
- Carga Bronze
- Transformação Bronze → Silver
- Agregações Gold
- Logging do pipeline
- Testes automatizados

---

# Testes implementados

O projeto possui testes automatizados para validar:

- extração dos dados;
- validação do schema;
- criação das tabelas;
- carga da Bronze;
- consultas analíticas da Gold;
- geração de logs.

---

# Como executar

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Configurar PostgreSQL

Criar o banco de dados e configurar as credenciais no arquivo:

```
config/settings.py
```

---

## Executar o pipeline

```bash
python main.py
```

---

## Executar os testes

```bash
pytest
```

---

# Próximas evoluções

Este projeto será expandido para incluir:

- Idempotência;
- UPSERT;
- Full Load;
- Incremental Load;
- Cursor de processamento;
- Recuperação de falhas;
- Tabela de controle de execução;
- Performance de ingestão utilizando COPY;
- Migração para PySpark;
- Orquestração com Airflow.

---

# Objetivo educacional

Este projeto faz parte do meu processo de formação em Engenharia de Dados.

O foco está na construção de pipelines organizados, seguindo boas práticas de arquitetura, qualidade de dados, automação e preparação para ambientes de produção.