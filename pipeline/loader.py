
import pandas as pd
from dotenv import load_dotenv
import psycopg2
import os
import logging
import csv
load_dotenv()



def salvar_csv(df:pd.DataFrame,caminho_arquivo:str):
    df.to_csv(caminho_arquivo,index=False)



def salvar_invalidos(registros_invalidos:list,caminho_arquivo:str):
    campos=['id_venda','id_cliente','filial','categoria','produto','quantidade','preco_unitario','desconto','vendedor','data_venda']

    with open(caminho_arquivo,'w',newline="",encoding='utf-8') as arquivo:
        escritor= csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for registro in registros_invalidos:
            escritor.writerow(registro)





def salvar_banco(df:pd.DataFrame):
    logging.info('Iniciando carga no postgres')
    query = """ INSERT INTO vendas (id_venda,id_cliente,filial,categoria,produto,quantidade,preco_unitario,desconto,vendedor,data_venda,valor_total)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    
    try:
        conexao = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
        cursor = conexao.cursor()

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
        logging.info('Carga realizada com sucesso')
    except psycopg2.Error as error:
        if 'conexao' in locals():
            conexao.rollback()
            logging.error(f'Erro ao carregar dados para postgres:{error}')
            raise
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()
    

