# Mini Pipeline V2 — Qualidade de Dados e Tratamento de Falhas

## Objetivo

Construir um pipeline ETL capaz de processar dados imperfeitos sem interromper a execução.

O foco não é apenas transformar dados.

O foco é:

* validar dados
* identificar erros
* contabilizar falhas
* gerar relatórios
* continuar executando mesmo com registros inválidos

---

# Conceitos que devo dominar

## Data Quality

Perguntas:

* O dado existe?
* O dado está no formato correto?
* O dado pode ser convertido?
* O dado respeita as regras de negócio?

---

## Resiliência

Um registro inválido não deve derrubar o pipeline inteiro.

Exemplo:

Entrada:

```csv
nome,idade,genero

Joao,25,male
Maria,trinta,female
Pedro,18,male
Ana,,female
```

Saída esperada:

* 2 registros válidos
* 2 registros inválidos
* pipeline finalizado com sucesso

---

# Estrutura do Projeto

```text
pipeline_v2/

├── input/
│   └── clientes.csv

├── output/
│   ├── clientes_processados.csv
│   └── relatorio.json

├── extract.py
├── transform.py
├── load.py
└── main.py
```

---

# Fase 1 — Extract

## Responsabilidade

Ler o CSV.

## Entregável

Função:

```python
extrair_dados()
```

Retorno:

```python
list[dict]
```

---

# Fase 2 — Transform

## Responsabilidade

Validar registros.

## Regras

### Nome

Inválido se:

```text
vazio
```

---

### Idade

Inválido se:

```text
vazia
não numérica
menor que 0
```

Converter para:

```python
int
```

---

### Gênero

Aceitar apenas:

```text
male
female
```

---

## Função

```python
transformar_dados()
```

Retornar:

```python
validos
invalidos
estatisticas
```

---

# Fase 3 — Métricas

Calcular:

```text
total_registros
validos
invalidos
idade_media
maior_idade
menor_idade
```

Não utilizar:

```python
max()
min()
```

---

# Fase 4 — Relatório de Erros

Contabilizar:

```text
idade_vazia
idade_invalida
nome_vazio
genero_invalido
```

Exemplo:

{
"idade_vazia": 3,
"idade_invalida": 2,
"nome_vazio": 1
}

---

# Fase 5 — Load CSV

Gerar:

```text
clientes_processados.csv
```

Somente registros válidos.

---

# Fase 6 — Load JSON

Gerar:

```text
relatorio.json
```

Exemplo:

{
"total": 100,
"validos": 80,
"invalidos": 20,
"idade_media": 32.5,
"maior_idade": 61,
"menor_idade": 18,
"erros": {
"idade_vazia": 8,
"idade_invalida": 7,
"nome_vazio": 5
}
}

---

# Simulações Obrigatórias

## Cenário 1

Idade vazia

```csv
Maria,
```

---

## Cenário 2

Idade inválida

```csv
Joao,trinta
```

---

## Cenário 3

Nome vazio

```csv
,25
```

---

## Cenário 4

Gênero inválido

```csv
Pedro,20,xyz
```

---

# Boss Fight V2

Receber um CSV com erros misturados.

Objetivo:

* extrair
* validar
* transformar
* gerar CSV limpo
* gerar JSON de métricas
* gerar relatório de erros

Sem quebrar o pipeline.

---

# Critério de Aprovação

✓ Separação ETL

✓ Uso de funções

✓ Uso de DictReader

✓ Uso de get()

✓ Uso de ValueError para regras de negócio

✓ CSV processado gerado

✓ JSON gerado

✓ Estatísticas corretas

✓ Relatório de erros correto

✓ Pipeline continua executando mesmo com registros inválidos
