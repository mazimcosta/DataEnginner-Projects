import pandas as pd
import psycopg2

from src.loader import salvar_banco, conectar


def test_upsert():

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Limpa caso exista de uma execução anterior
        cursor.execute(
            "DELETE FROM bronze_mercado WHERE id_venda = 999"
        )
        conexao.commit()

        # -------------------------
        # Primeira carga (INSERT)
        # -------------------------
        df = pd.DataFrame(
            [
                {
                    "id_venda": 999,
                    "data_venda": "2026-07-10",
                    "id_cliente": 999,
                    "nome_cliente": "Cliente Teste",
                    "cidade": "Maceio",
                    "categoria": "Teste",
                    "produto": "Produto",
                    "quantidade": 1,
                    "preco_unitario": 10,
                    "desconto": 0,
                    'status_pagamento':'pago'
                }
            ]
        )

        salvar_banco(df)

        # -------------------------
        # Segunda carga (UPDATE)
        # -------------------------
        df.loc[0, "desconto"] = 5

        salvar_banco(df)

        # -------------------------
        # Validação
        # -------------------------
        cursor.execute("""
            SELECT COUNT(*)
            FROM bronze_mercado
            WHERE id_venda = 999
        """)

        quantidade = cursor.fetchone()[0]

        cursor.execute("""
            SELECT desconto
            FROM bronze_mercado
            WHERE id_venda = 999
        """)

        desconto = cursor.fetchone()[0]

        assert quantidade == 1
        assert desconto == 5

    finally:

        cursor.execute(
            "DELETE FROM bronze_mercado WHERE id_venda = 999"
        )
        conexao.commit()

        cursor.close()
        conexao.close()
    
