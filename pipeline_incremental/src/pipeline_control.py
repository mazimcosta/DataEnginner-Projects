
import pandas as pd
import psycopg2

from src.database import conectar
from src.logger import logger


def buscar_ultimo_id(nome_pipeline: str) -> int:
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT ultimo_id_processado
            FROM pipeline_controle
            WHERE nome_pipeline = %s
            """,
            (nome_pipeline,),
        )

        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError(
                f"Pipeline não encontrado: {nome_pipeline}"
            )

        ultimo_id_processado = int(resultado[0])

        return ultimo_id_processado

    except psycopg2.Error:
        if conexao:
            conexao.rollback()

        logger.exception(
            "Falha ao consultar o último ID processado"
        )
        raise

    finally:
        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def filtrar_registros(
    df: pd.DataFrame,
    ultimo_id: int,
) -> pd.DataFrame:
    if df.empty:
        raise ValueError(
            "Não é possível filtrar um DataFrame vazio"
        )

    df_filtrado = df[
        df["id_venda"] > ultimo_id
    ].copy()

    return df_filtrado


def obter_maior_id(df: pd.DataFrame) -> int:
    if df.empty:
        raise ValueError(
            "Não é possível obter o maior ID de um DataFrame vazio"
        )

    maior_id = int(
        df["id_venda"].max()
    )

    return maior_id


def registrar_ultimo_id(
    ultimo_id: int,
    nome_pipeline: str,
) -> None:
    conexao = None
    cursor = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE pipeline_controle
            SET
                ultimo_id_processado = %s,
                atualizado_em = CURRENT_TIMESTAMP
            WHERE nome_pipeline = %s
            """,
            (
                ultimo_id,
                nome_pipeline,
            ),
        )

        if cursor.rowcount == 0:
            raise ValueError(
                f"Pipeline não encontrado: {nome_pipeline}"
            )

        conexao.commit()

    except psycopg2.Error:
        if conexao:
            conexao.rollback()

        logger.exception(
            "Falha ao atualizar o último ID processado"
        )
        raise

    finally:
        if cursor:
            cursor.close()

        if conexao:
            conexao.close()