
import psycopg2
from src.loader import conectar
from src.logger import logger


def executar_sql(caminho_arquivo):
    conexao=None
    cursor=None

    try:
        conexao=conectar()
        cursor=conexao.cursor()

            
        with open(caminho_arquivo,'r',encoding='utf-8') as arquivo:
            query=arquivo.read()
        
        cursor.execute(query)
        conexao.commit()
        logger.info(f'Sql executado com sucesso:{caminho_arquivo}')
    
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