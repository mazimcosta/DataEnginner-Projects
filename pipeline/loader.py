
import pandas as pd
from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()

def salvar_csv(df:pd.DataFrame,caminho_arquivo:str):
    df.to_csv(caminho_arquivo,index=False)


def salvar_banco(df:pd.DataFrame):
    conexao = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    query = """ INSERT INTO vendas (id_venda,id_cliente,filial,categoria,produto,quantidade,preco_unitario,desconto,vendedor,data_venda,valor_total)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor = conexao.cursor()
    try:
        for linha in df.itertuples():
            cursor.execute(query,(
                linha.id_venda,
                linha.id_cliente,
                linha.filial,
                linha.categoria,
                linha.produto,
                linha.quantidade,
                linha.preco_unitario,
                linha.desconto,
                linha.vendedor,
                linha.data_venda,
                linha.valor_total
            ))
        conexao.commit()

    except Exception as error:
        if 'conexao' in locals():
            conexao.rollback()
            print(error)
    
    finally:
        cursor.close()
        conexao.close()
