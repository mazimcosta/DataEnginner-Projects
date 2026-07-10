import psycopg2
import pandas as pd
import csv
from dotenv import load_dotenv
from config.settings import ENV_FILE
load_dotenv(ENV_FILE)
import os
from src.logger import logger

def conectar():
    conexao=psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
    return conexao
    

def salvar_csv_valido(df:pd.DataFrame,caminho_arquivo):

    df.to_csv(caminho_arquivo,index=False)


def salvar_csv_invalidos(registros_invalidos:list,caminho_arquivo:str):

    campos=['cliente','produto','categoria','quantidade','preco_unitario','data_venda']

    with open(caminho_arquivo,'w',newline="",encoding='utf-8') as arquvo:

        escritor=csv.DictWriter(arquvo,fieldnames=campos)
        escritor.writeheader()
        for registro in registros_invalidos:
            escritor.writerow(registro)


def salvar_banco(df:pd.DataFrame):
    cursor=None
    conexao=None
    query=""" INSERT INTO bronze_mercado (id_venda,data_venda,id_cliente,nome_cliente,cidade,categoria,produto,quantidade,preco_unitario,desconto,status_pagamento)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    try:
        conexao=conectar()
        cursor=conexao.cursor()

        for linha in df.itertuples():
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


