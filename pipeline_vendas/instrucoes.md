==================================================
PARTE 2 — ENUNCIADO DO PIPELINE V3
==================================================

OBJETIVO

Construir um novo pipeline usando transfer learning.

Você NÃO deve copiar o Pipeline V2 linha por linha.

Você deve reutilizar a arquitetura mental:

Extract
↓
Validate Schema
↓
Transform
↓
Load

==================================================
ESTRUTURA ESPERADA

pipeline_v3/

├── input/
│   └── vendas.csv

├── output/
│   ├── vendas_validas.csv
│   └── relatorio.json

├── extract.py
├── schema.py
├── transform.py
├── load.py
└── main.py

==================================================
SCHEMA OBRIGATÓRIO

O arquivo deve conter as colunas:

produto
preco
quantidade
categoria

Se faltar alguma coluna, o pipeline deve parar com erro controlado.

==================================================
VALIDAÇÕES

produto:
- inválido se vazio
- inválido se tiver apenas espaços

preco:
- inválido se vazio
- inválido se não puder virar float
- inválido se menor ou igual a 0

quantidade:
- inválida se vazia
- inválida se não puder virar int
- inválida se menor ou igual a 0

categoria:
- inválida se vazia
- inválida se tiver apenas espaços

==================================================
TRANSFORMAÇÃO

Para cada venda válida, criar nova coluna:

faturamento

Regra:

faturamento = preco * quantidade

Exemplo:

produto: Notebook
preco: 3500.00
quantidade: 2

faturamento: 7000.00

==================================================
SAÍDA CSV

Gerar:

output/vendas_validas.csv

Colunas:

produto,preco,quantidade,categoria,faturamento

Somente registros válidos devem aparecer.

==================================================
SAÍDA JSON

Gerar:

output/relatorio.json

Deve conter:

total_registros
validos
invalidos
faturamento_total
erros

Erros esperados:

produto_vazio
preco_vazio
preco_invalido
preco_negativo_ou_zero
quantidade_vazia
quantidade_invalida
quantidade_negativa_ou_zero
categoria_vazia

==================================================
CRITÉRIO DE APROVAÇÃO

O pipeline deve:

1. Ler vendas.csv
2. Validar schema
3. Separar vendas válidas e inválidas
4. Gerar vendas_validas.csv
5. Gerar relatorio.json
6. Calcular faturamento por venda
7. Calcular faturamento_total
8. Não quebrar com dados inválidos
9. Não usar pandas
10. Não usar except genérico

==================================================
RESTRIÇÕES

Não usar:

pandas
sqlalchemy
postgresql
docker
airflow
spark

Usar apenas:

csv
json
funções
dict
list
try/except específico
raise ValueError para erro de schema