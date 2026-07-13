import csv
import psycopg2
import pandas as pd
from src.database import conectar
from src.logger import logger

def salvar_csv_valido(df:pd.DataFrame,caminho_arquivo:str):

    df.to_csv(caminho_arquivo,index=False)


def salvar_csv_invalido(registros_invalidos:list,caminho_arquivo:str):

    campos=['id_venda','data_venda','id_cliente','nome_cliente','cidade','categoria','produto','quantidade','preco_unitario','desconto','status_pagamento']

    with open(caminho_arquivo,'w',newline="",encoding='utf-8') as arquivo:

        escritor=csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for registro in registros_invalidos:
            escritor.writerow(registro)

def salvar_banco(df:pd.DataFrame):
    conexao=None
    cursor=None

    query=""" INSERT INTO bronze_farmacia(
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
    status_pagamento)
    VALUES(
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s)
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
    status_pagamento = EXCLUDED.status_pagamento;"""

    try:
        conexao=conectar()
        cursor=conexao.cursor()

        for linha in df.itertuples(index=False):
            cursor.execute(query,(
                linha.id_venda,
                linha.data_venda,
                linha.id_cliente,
                linha.nome_cliente,
                linha.cidade,
                linha.categoria,
                linha.produto,
                linha.quantidade,
                linha.preco_unitario,
                linha.desconto,
                linha.status_pagamento
            ))

        conexao.commit()
    
    except psycopg2.Error as error:
        if conexao:
            conexao.rollback()
        logger.error(f'Falha na carga do banco:{error}')
        raise

    finally:
        if cursor:
            cursor.close()

        if conexao:
            conexao.close()
