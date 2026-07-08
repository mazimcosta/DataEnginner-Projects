# Boss Pipeline

Pipeline de dados desenvolvido como parte do meu roadmap de estudos em Engenharia de Dados. O projeto tem como objetivo praticar boas práticas de desenvolvimento, organização em camadas, validação de dados e testes automatizados utilizando Python.

---

# Objetivos

- Construir um pipeline de dados modular.
- Aplicar separação de responsabilidades.
- Validar dados utilizando Pydantic.
- Transformar e padronizar dados com Pandas.
- Praticar testes automatizados com Pytest.
- Desenvolver código limpo e de fácil manutenção.

---

# Arquitetura

```text
CSV
 │
 ▼
Extractor
 │
 ▼
Schema (Pydantic)
 │
 ▼
Transformer
 │
 ▼
Loader
 │
 ▼
Pipeline
```

Cada módulo possui uma responsabilidade específica, facilitando manutenção, testes e evolução do projeto.

---

# Estrutura do Projeto

```text
boss_pipeline/
│
├── config/
│   ├── __init__.py
│   ├── .env
│   └── settings.py
│
├── data/
│   ├── input/
│   └── output/
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── extractor.py
│   ├── schema.py
│   ├── transformer.py
│   ├── loader.py
│   ├── pipeline.py
│   └── logger.py
│
├── tests/
│   ├── test_schema.py
│   └── test_transformer.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Fluxo do Pipeline

1. Extração dos dados do arquivo CSV.
2. Validação dos registros com Pydantic.
3. Limpeza e transformação dos dados.
4. Carregamento do resultado final.
5. Registro das etapas em log.

---

# Tecnologias Utilizadas

- Python 3.13
- Pandas
- Pydantic
- Pytest
- Pathlib
- Logging

---

# Funcionalidades

## Extração

- Leitura de arquivos CSV.
- Tratamento do caminho dos arquivos.

## Validação

- Campos obrigatórios.
- Tipagem.
- Regras de negócio.

## Transformação

- Padronização de textos.
- Conversão de preços.
- Tratamento de valores.
- Remoção de registros inválidos.

## Carregamento

- Escrita do dataset tratado.

## Logs

- Registro da execução do pipeline.

---

# Testes Automatizados

O projeto utiliza **Pytest** para validar o comportamento das principais regras de negócio.

Atualmente a suíte contempla testes para:

- Validação de Schema.
- Transformações.
- Casos válidos.
- Casos inválidos.
- Regras de negócio.

Execução:

```bash
pytest tests/
```

Resultado atual:

```text
==================== 20 passed ====================
```

---

# Como executar

Clone o projeto:

```bash
git clone <url-do-repositorio>
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o pipeline:

```bash
python main.py
```

Execute os testes:

```bash
pytest tests/
```

---

# Próximas Evoluções

- GitHub Actions para integração contínua.
- PostgreSQL como camada de persistência.
- SQL Analítico.
- Modelagem Dimensional.
- Data Warehouse.
- PySpark.
- dbt.

---

# Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

- Organização em camadas.
- Separação de responsabilidades.
- Código limpo.
- Validação de dados.
- Tratamento de exceções.
- Testes automatizados.
- Documentação técnica.

Este projeto faz parte da construção de um roadmap de longo prazo com foco em Engenharia de Dados e evolução contínua das práticas de desenvolvimento.