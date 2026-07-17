
INSERT INTO silver_cafe(
    transacao_id,
    id_incremental,
    produto,
    quantidade,
    preco_unitario,
    valor_total,
    metodo_pagamento,
    localidade,
    data_transacao,
    mes,
    ano
)
SELECT
transacao_id,
id_incremental,
produto,
quantidade,
preco_unitario,
valor_total,
metodo_pagamento,
localidade,
data_transacao,
EXTRACT(MONTH FROM data_transacao),
EXTRACT(YEAR FROM data_transacao)
FROM bronze_cafe
ON CONFLICT (transacao_id)
DO UPDATE SET
id_incremental = EXCLUDED.id_incremental,
produto = EXCLUDED.produto,
quantidade = EXCLUDED.quantidade,
preco_unitario = EXCLUDED.preco_unitario,
valor_total = EXCLUDED.valor_total,
metodo_pagamento = EXCLUDED.metodo_pagamento,
localidade = EXCLUDED.localidade,
mes = EXCLUDED.mes,
ano = EXCLUDED.ano;


INSERT INTO gold_faturamento_produto(
    produto,
    faturamento_total
)
SELECT
produto,
SUM(valor_total)
FROM silver_cafe
GROUP BY produto;

INSERT INTO gold_venda_produto(
    produto,
    venda_total
)
SELECT
produto,
SUM(quantidade)
FROM silver_cafe
GROUP BY produto;

INSERT INTO gold_faturamento_localidade(
    localidade,
    faturamento_total
)
SELECT
localidade,
SUM(valor_total)
FROM silver_cafe
GROUP BY localidade;


INSERT INTO gold_faturamento_mes(
    mes,
    ano,
    faturamento_total
)
SELECT
mes,
ano,
SUM(valor_total)
FROM silver_cafe
GROUP BY mes,ano;

INSERT INTO gold_faturamento_ano(
    ano,
    faturamento_total
)
SELECT
ano,
SUM(valor_total)
FROM silver_cafe
GROUP BY ano;