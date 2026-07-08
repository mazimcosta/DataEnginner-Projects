
import pandas as pd
from dotenv import load_dotenv
import os
import psycopg2
load_dotenv()

def salvar_csv(df:pd.DataFrame,caminho_arquivo:str):
    df.to_csv(caminho_arquivo,index=False)

def salvar_banco(df:pd.DataFrame):

    conexao=psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    cursor=conexao.cursor()
    query=""" INSERT INTO entregas (id_entrega,id_cliente,filial,cidade,motorista,status_entrega,peso_kg,valor_frete,data_entrega,valor_por_kg)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    try:
        for linha in df.itertuples():
            cursor.execute(query,(
                linha.id_entrega,
                linha.id_cliente,
                linha.filial,
                linha.cidade,
                linha.motorista,
                linha.status_entrega,
                linha.peso_kg,
                linha.valor_frete,
                linha.data_entrega,
                linha.valor_por_kg
            ))
        conexao.commit()
    except Exception as error:
        if 'conexao' in locals():
            conexao.rollback()
            print(error)
    
    finally:
        cursor.close()
        conexao.close()