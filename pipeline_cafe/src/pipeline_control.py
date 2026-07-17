import pandas as pd
import psycopg2
from src.logger import logger
from src.database import conectar

def buscar_ultimo_id(nome_pipeline:str) -> int:
    conexao=None
    cursor= None

    try:
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""SELECT ultimo_id_processado FROM pipeline_controle WHERE nome_pipeline = %s """,(nome_pipeline,))
        resultado=cursor.fetchone()
        if resultado is None:
            raise ValueError(f'Pipeline nao encontrado: {nome_pipeline}')
        ultimo_id=resultado[0]
        return ultimo_id
    
    except psycopg2.Error:
        logger.exception('Falha na busca do ultimo_id')
        raise

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def filtrar_novos_registros(df:pd.DataFrame,ultimo_id:int) -> pd.DataFrame:

    if df.empty:
        raise ValueError('Erro dataframe vazio.')
    df_filtrado=df[df['id_incremental']> ultimo_id]
    return df_filtrado


def obter_maior_id(df:pd.DataFrame) -> int:
    if df.empty:
        raise ValueError('Erro dataframe vazio')
    ultimo_id=int(df['id_incremental'].max())
    return ultimo_id

def atualizar_ultimo_id(ultimo_id:int,nome_pipeline:str) -> None:

    conexao=None
    cursor=None

    try:
        conexao=conectar()
        cursor=conexao.cursor()

        cursor.execute("""UPDATE pipeline_controle SET ultimo_id_processado = %s WHERE nome_pipeline = %s """,(ultimo_id,nome_pipeline))
        if cursor.rowcount ==0:
            raise ValueError('Nao foi possivel atualizar ultimo_id')
        conexao.commit()

    except psycopg2.Error:
        if conexao:
            conexao.rollback()
        logger.exception('Erro na atualizacao do ultimo_id')
        raise

    finally:
        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


