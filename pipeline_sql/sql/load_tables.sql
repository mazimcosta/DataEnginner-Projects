
INSERT INTO silver_mercado(
    id_venda,
    data_venda,
    id_cliente,
    nome_cliente,
    cidade,
    categoria,
    produto,
    quantidade,
    preco_unitario,
    desconto,
    valor_bruto,
    valor_liquido
)
SELECT
id_venda,
data_venda,
id_cliente,
nome_cliente,
cidade,
categoria,
produto,
quantidade,
preco_unitario,
desconto,
preco_unitario * quantidade,
(preco_unitario * quantidade) - desconto
FROM bronze_mercado
WHERE quantidade>0 AND status_pagamento = 'pago' AND preco_unitario>0;

INSERT INTO gold_faturamento_categoria(
    categoria,
    faturamento_total
)
SELECT
categoria,
SUM(valor_liquido)
FROM silver_mercado
GROUP BY categoria
ORDER BY SUM(valor_liquido) DESC;

INSERT INTO gold_faturamento_cliente(
    nome_cliente,
    faturamento_total

)
SELECT
nome_cliente,
SUM(valor_liquido)
FROM silver_mercado
GROUP BY nome_cliente
ORDER BY SUM(valor_liquido) DESC;

INSERT INTO gold_faturamento_cidade(
    cidade,
    faturamento_total
)
SELECT
cidade,
SUM(valor_liquido)
FROM silver_mercado
GROUP BY cidade
ORDER BY SUM(valor_liquido) DESC;

INSERT INTO gold_vendas_dia(
    data_venda,
    faturamento_total
)
SELECT
data_venda,
SUM(valor_liquido)
FROM silver_mercado
GROUP BY data_venda
ORDER BY SUM(valor_liquido) DESC;