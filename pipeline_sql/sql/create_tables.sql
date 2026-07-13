
CREATE TABLE IF NOT EXISTS bronze_mercado(
    id_venda INTEGER NOT NULL PRIMARY KEY,
    data_venda DATE NOT NULL,
    id_cliente INTEGER NOT NULL,
    nome_cliente VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    produto VARCHAR(50) NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario NUMERIC(8,2) NOT NULL,
    desconto NUMERIC(8,2) NOT NULL,
    status_pagamento VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS silver_mercado(
    id_venda INTEGER NOT NULL PRIMARY KEY,
    data_venda DATE NOT NULL,
    id_cliente INTEGER NOT NULL,
    nome_cliente VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    produto VARCHAR(50) NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario NUMERIC(8,2) NOT NULL,
    desconto NUMERIC(8,2) NOT NULL,
    valor_bruto NUMERIC(8,2) NOT NULL,
    valor_liquido NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_faturamento_categoria(
    categoria VARCHAR(50) NOT NULL PRIMARY KEY,
    faturamento_total NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_faturamento_cliente(
    id_cliente INTEGER NOT NULL PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL,
    faturamento_total  NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_faturamento_cidade(
    cidade VARCHAR(100) NOT NULL PRIMARY KEY,
    faturamento_total NUMERIC(8,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS gold_vendas_dia(
    data_venda DATE NOT NULL PRIMARY KEY,
    faturamento_total  NUMERIC(8,2) NOT NULL
)