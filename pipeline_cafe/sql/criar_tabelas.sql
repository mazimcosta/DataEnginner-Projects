
CREATE TABLE IF NOT EXISTS bronze_cafe(
    transacao_id VARCHAR(100) NOT NULL PRIMARY KEY,
    id_incremental INTEGER NOT NULL UNIQUE,
    produto VARCHAR(100) NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario NUMERIC(8,2) NOT NULL,
    valor_total NUMERIC(8,2) NOT NULL,
    metodo_pagamento VARCHAR(100) NOT NULL,
    localidade VARCHAR(100) NOT NULL,
    data_transacao DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS silver_cafe(
    transacao_id VARCHAR(100) NOT NULL PRIMARY KEY,
    id_incremental INTEGER NOT NULL UNIQUE,
    produto VARCHAR(100) NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario NUMERIC(8,2) NOT NULL,
    valor_total NUMERIC(8,2) NOT NULL,
    metodo_pagamento VARCHAR(100) NOT NULL,
    localidade VARCHAR(100) NOT NULL,
    data_transacao DATE NOT NULL,
    mes INTEGER NOT NULL,
    ano INTEGER NOT NULL
);


CREATE TABLE IF NOT EXISTS gold_faturamento_produto(
    produto VARCHAR(100) NOT NULL PRIMARY KEY,
    faturamento_total NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_venda_produto(
    produto VARCHAR(100) NOT NULL PRIMARY KEY,
    venda_total INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_faturamento_localidade(
    localidade VARCHAR(100) NOT NULL PRIMARY KEY,
    faturamento_total NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_faturamento_mes(
    ano INTEGER NOT NULL,
    mes INTEGER NOT NULL,
    faturamento_total NUMERIC(8,2) NOT NULL,
    PRIMARY KEY(ano,mes)
);

CREATE TABLE IF NOT EXISTS gold_faturamento_ano(
    ano INTEGER NOT NULL PRIMARY KEY,
    faturamento_total NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS pipeline_controle(
    nome_pipeline VARCHAR(100) NOT NULL PRIMARY KEY,
    ultimo_id_processado INTEGER NOT NULL,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO pipeline_controle(
    nome_pipeline,
    ultimo_id_processado
)
VALUES(
    'cafe',
    0
)
ON CONFLICT (nome_pipeline)
DO NOTHING;
