# Pipeline ETL de Vendas

## 📖 Sobre o Projeto

Este projeto implementa um pipeline ETL (Extract, Transform, Load) utilizando Python, Pandas e PostgreSQL.

O objetivo é realizar a leitura de um arquivo CSV contendo dados de vendas com inconsistências, aplicar regras de limpeza e transformação e carregar apenas os registros válidos para um banco de dados PostgreSQL.

O projeto foi desenvolvido com foco em boas práticas de organização de código, separação de responsabilidades e pensamento de engenharia.

---

# Tecnologias Utilizadas

- Python 3
- Pandas
- PostgreSQL
- Psycopg2
- python-dotenv

---

# Estrutura do Projeto

```
pipeline/

│

├── extractor.py      # Leitura do CSV

├── transformer.py    # Limpeza e transformação dos dados

├── loader.py         # Persistência no PostgreSQL

├── pipeline.py       # Orquestração do ETL

├── main.py           # Ponto de entrada da aplicação

├── vendas_sujas.csv

├── output/

│   └── vendas.csv

├── .env

└── README.md
```

---

# Fluxo do Pipeline

```
CSV

↓

Extractor

↓

Transformer

↓

Loader

↓

PostgreSQL
```

---

# Responsabilidade de Cada Módulo

## extractor.py

Responsável por:

- Ler o arquivo CSV.
- Retornar um DataFrame.

---

## transformer.py

Responsável por:

- Padronizar textos.
- Corrigir valores monetários.
- Tratar valores ausentes.
- Aplicar regras de negócio.
- Remover registros inválidos.
- Calcular a coluna `valor_total`.

---

## loader.py

Responsável por:

- Salvar o DataFrame em CSV.
- Conectar ao PostgreSQL.
- Inserir os registros.
- Realizar commit da transação.
- Encerrar conexão e cursor.

---

## pipeline.py

Responsável apenas por orquestrar o fluxo:

1. Extrair
2. Transformar
3. Carregar

---

## main.py

Responsável por iniciar o pipeline.

---

# Regras de Negócio Aplicadas

- Padronização de nomes de vendedores.
- Padronização de categorias.
- Padronização das filiais.
- Conversão de valores monetários.
- Tratamento de registros com informações ausentes.
- Cálculo do valor total da venda.
- Remoção de registros inválidos.

---

# Principais Desafios

Durante o desenvolvimento surgiram alguns desafios importantes:

- Conversão de preços em diferentes formatos.
- Tratamento de valores inconsistentes.
- Correção de nomes escritos de formas diferentes.
- Separação correta das responsabilidades entre os módulos.
- Persistência dos dados no PostgreSQL utilizando transações.

---

# Principais Aprendizados

Este projeto reforçou conceitos importantes de Engenharia de Dados:

- Separação de responsabilidades.
- Organização de pipelines ETL.
- Limpeza e qualidade dos dados.
- Uso do Pandas para transformação de dados.
- Persistência utilizando PostgreSQL.
- Importância do commit em transações.
- Organização de projetos Python.

---

# Como Executar

## 1. Instalar as dependências

```bash
pip install pandas psycopg2 python-dotenv
```

---

## 2. Configurar o arquivo `.env`

```
DB_NAME=seu_banco
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

---

## 3. Executar

```bash
python main.py
```

---

# Resultado Esperado

Após a execução:

- Os dados limpos são exportados para um novo CSV.
- Os registros válidos são inseridos no PostgreSQL.
- Apenas dados consistentes permanecem na base.

---

# Próximos Passos

Este projeto representa a primeira implementação de um pipeline ETL.

Os próximos objetivos são:

- Implementar logs.
- Adicionar testes automatizados.
- Utilizar Docker.
- Automatizar execuções.
- Trabalhar com múltiplas fontes de dados.
- Evoluir para pipelines escaláveis.

---

## Autor

Desenvolvido como parte do meu roadmap de formação em Engenharia de Dados, com foco em construção de projetos reais, pensamento de engenharia e boas práticas de desenvolvimento.