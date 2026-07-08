
import psycopg2
import csv
import pandas as pd
from dotenv import load_dotenv
from src.logger import logger
from config.settings import ENV_FILE
import os
load_dotenv(ENV_FILE)

def salvar_csv_valido(df:pd.DataFrame,caminho_arquivo:str):

    df.to_csv(caminho_arquivo,index=False)

def salvar_csv_invalido(registros_invalidos:list,caminho_arquivo:str):
    campos=['id_pedido','mesa','item','categoria','quantidade','preco_unitario','status','pagamento','valor_total']

    with open(caminho_arquivo,'w',newline="",encoding='utf-8') as arquivo:
        escritor=csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for registro in registros_invalidos:
            escritor.writerow(registro)


def salvar_banco(df:pd.DataFrame):
    conexao=None
    cursor=None
    query=""" INSERT INTO pedidos (id_pedido,mesa,item,categoria,quantidade,preco_unitario,status,pagamento,valor_total)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    try:
        conexao=psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        cursor=conexao.cursor()
        for linha in df.itertuples():
            cursor.execute(query,(
                linha.id_pedido,
                linha.mesa,
                linha.item,
                linha.categoria,
                linha.quantidade,
                linha.preco_unitario,
                linha.status,
                linha.pagamento,
                linha.valor_total
            ))
        conexao.commit()
    except psycopg2.Error as error:
        if conexao:
            conexao.rollback()
            logger.error(f'Erro falha na carga do banco:{error}')
    
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()