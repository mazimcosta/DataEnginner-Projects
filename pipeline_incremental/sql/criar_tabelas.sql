
CREATE TABLE IF NOT EXISTS bronze_farmacia(
    id_venda INTEGER NOT NULL PRIMARY KEY,
    data_venda DATE NOT NULL,
    id_cliente INTEGER NOT NULL,
    nome_cliente VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    produto VARCHAR(100) NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario NUMERIC(8,2) NOT NULL,
    desconto NUMERIC(8,2) NOT NULL,
    status_pagamento VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS silver_farmacia(
    id_venda INTEGER NOT NULL PRIMARY KEY,
    data_venda DATE NOT NULL,
    id_cliente INTEGER NOT NULL,
    nome_cliente VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    produto VARCHAR(100) NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario NUMERIC(8,2) NOT NULL,
    desconto NUMERIC(8,2) NOT NULL,
    valor_bruto NUMERIC(8,2) NOT NULL,
    valor_liquido NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_faturamento_categoria(
    categoria VARCHAR(100) NOT NULL PRIMARY KEY,
    faturamento_total NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_faturamento_cidade(
    cidade VARCHAR(100) NOT NULL PRIMARY KEY,
    faturamento_total NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_faturamento_cliente(
    id_cliente INTEGER NOT NULL PRIMARY KEY,
    faturamento_total NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_produto_vendido(
    produto VARCHAR(100) NOT NULL PRIMARY KEY,
    faturamento_total NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_quantidade_produto(
    produto VARCHAR(100) NOT NULL PRIMARY KEY,
    quantidade_total INTEGER NOT NULL
);

CREATE TABLE IF NOT  EXISTS pipeline_controle (
    nome_pipeline VARCHAR(100)  PRIMARY KEY,
    ultimo_id_processado INTEGER NOT NULL DEFAULT (0),
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO pipeline_controle (
    nome_pipeline,
    ultimo_id_processado
    
)
VALUES(
    'pipeline_incremental',
    0
)
ON CONFLICT (nome_pipeline)
DO NOTHING;