# Evolução de Pipelines de Dados com Python e PostgreSQL

Este repositório reúne uma sequência de projetos desenvolvidos durante minha formação em Engenharia de Dados.

Cada projeto representa uma etapa da evolução de um pipeline: desde a leitura e validação básica de arquivos CSV até uma arquitetura em camadas Bronze, Silver e Gold, com PostgreSQL, validação de dados, logging, testes automatizados, carga incremental e idempotência.

O objetivo do repositório não é apresentar apenas o resultado final, mas demonstrar como os projetos foram evoluindo conforme novos problemas de engenharia foram identificados e resolvidos.

---

## Objetivo do repositório

Demonstrar, por meio de projetos progressivos, a construção de pipelines de dados cada vez mais confiáveis, organizados e próximos de um ambiente profissional.

Durante essa evolução, foram trabalhados conceitos como:

- extração, transformação e carga de dados;
- processamento de arquivos CSV e JSON;
- validação de estrutura e regras de negócio;
- separação de responsabilidades;
- transformação de dados com Python, Pandas e SQL;
- integração com PostgreSQL;
- tratamento de exceções;
- logging estruturado;
- testes unitários;
- arquitetura Medallion;
- carga incremental;
- UPSERT;
- idempotência;
- investigação de falhas;
- qualidade e organização de código.

---

## Evolução dos projetos

```text
Pipeline simples
      ↓
Validação e geração de relatórios
      ↓
ET
