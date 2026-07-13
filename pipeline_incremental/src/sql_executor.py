from src.database import conectar
import psycopg2
from src.logger import logger


def executar_sql(caminho_arquivo:str):

    conexao= None
    cursor=None

    try:
        with open(caminho_arquivo,'r',encoding='utf-8') as arquivo:
            query=arquivo.read()

        conexao=conectar()
        cursor=conexao.cursor()
        cursor.execute(query)
        conexao.commit()

    except psycopg2.Error as error:
        if conexao:
            conexao.rollback()
        logger.error(f'Falha na execucao do sql:{error}')
        raise

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

        