
import csv
import pandas as pd
import psycopg2
from src.logger import logger
from src.database import conectar


def salvar_csv_valido(df:pd.DataFrame,caminho_arquivo:str) -> None:

    df.to_csv(caminho_arquivo,index=False)


def salvar_csv_invalidos(registros_invalidos:list,caminho_arquivo:str) -> None:

    campos=['transacao_id','produto','id_incremental','quantidade','preco_unitario','valor_total','metodo_pagamento','localidade','data_transacao','motivo_erro']

    with open(caminho_arquivo,'w',newline="",encoding='utf-8') as arquivo:

        escritor=csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for registro in registros_invalidos:
            escritor.writerow(registro)


def salvar_banco(df:pd.DataFrame) -> None:
    logger.info('Iniciando carga na bronze')

    conexao=None
    cursor= None
    query="""INSERT INTO bronze_cafe (
    transacao_id,
    id_incremental,
    produto,
    quantidade,
    preco_unitario,
    valor_total,
    metodo_pagamento,
    localidade,
    data_transacao)
    VALUES(
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s)
    ON CONFLICT (transacao_id)
    DO UPDATE SET
    produto = EXCLUDED.produto,
    quantidade = EXCLUDED.quantidade,
    preco_unitario = EXCLUDED.preco_unitario,
    valor_total = EXCLUDED.valor_total,
    metodo_pagamento = EXCLUDED.metodo_pagamento,
    localidade = EXCLUDED.localidade,
    data_transacao = EXCLUDED.data_transacao;"""

    lista=[]

    for linha in df.itertuples(index=False):
        lista.append((linha.transacao_id,linha.id_incremental,linha.produto,linha.quantidade,linha.preco_unitario,linha.valor_total,linha.metodo_pagamento,linha.localidade,linha.data_transacao))

    try:
        conexao=conectar()
        cursor= conexao.cursor()
        cursor.executemany(query,lista)
        conexao.commit()
        logger.info(f'{len(lista)} registros inseridos na bronze')

    except psycopg2.Error:
        if conexao:
            conexao.rollback()
        logger.exception('Erro na insercao da bronze')
        raise

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()



