import psycopg2
from src.database import conectar
from src.logger import logger

def executar_sql(caminho_arquivo:str) -> None:
    conexao=None
    cursor=None

    with open(caminho_arquivo,'r',encoding='utf-8') as arquivo:
        
        query=arquivo.read()

    try:
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute(query)
        conexao.commit()

    except psycopg2.Error:
        if conexao:
            conexao.rollback()
        logger.exception('Falha na carga do banco')
        raise

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
    