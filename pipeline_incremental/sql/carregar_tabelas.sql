
INSERT INTO silver_farmacia(
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
FROM bronze_farmacia
WHERE quantidade>0 AND preco_unitario>0 AND status_pagamento = 'pago'
ON CONFLICT (id_venda)
DO UPDATE SET
data_venda = EXCLUDED.data_venda,
id_cliente = EXCLUDED.id_cliente,
nome_cliente = EXCLUDED.nome_cliente,
cidade = EXCLUDED.cidade,
categoria = EXCLUDED.categoria,
produto = EXCLUDED.produto,
quantidade = EXCLUDED.quantidade,
preco_unitario = EXCLUDED.preco_unitario,
desconto = EXCLUDED.desconto,
valor_bruto = EXCLUDED.valor_bruto,
valor_liquido = EXCLUDED.valor_liquido;

INSERT INTO gold_faturamento_categoria(
    categoria,
    faturamento_total
)
SELECT
categoria,
SUM(valor_liquido)
FROM silver_farmacia
GROUP BY categoria
ORDER BY SUM(valor_liquido) DESC;

INSERT INTO gold_faturamento_cliente(
    id_cliente,
    faturamento_total
)
SELECT
id_cliente,
SUM(valor_liquido)
FROM silver_farmacia
GROUP BY id_cliente
ORDER BY SUM(valor_liquido) DESC;


INSERT INTO gold_faturamento_cidade(
    cidade,
    faturamento_total
)
SELECT
cidade,
SUM(valor_liquido)
FROM silver_farmacia
GROUP BY cidade
ORDER BY SUM(valor_liquido) DESC;

INSERT INTO gold_produto_vendido(
    produto,
    faturamento_total
)
SELECT
produto,
SUM(valor_liquido)
FROM silver_farmacia
GROUP BY produto
ORDER BY SUM(valor_liquido) DESC;

INSERT INTO gold_quantidade_produto(
    produto,
    quantidade_total
)
SELECT
produto,
SUM(quantidade)
FROM silver_farmacia
GROUP BY produto
ORDER BY SUM(quantidade) DESC;
