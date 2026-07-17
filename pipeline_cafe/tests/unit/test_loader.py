import pandas as pd
import pytest
from src.loader import salvar_csv_invalidos,salvar_banco,salvar_csv_valido

import pandas as pd

from src.loader import (
    salvar_csv_invalidos,
    salvar_csv_valido,
)


def test_salvar_csv_valido_cria_arquivo_com_as_linhas(
    tmp_path,
):
    # Preparação
    df = pd.DataFrame(
        [
            {
                "transacao_id": "TXN_001",
                "produto": "Coffee",
                "quantidade": 2,
            },
            {
                "transacao_id": "TXN_002",
                "produto": "Tea",
                "quantidade": 3,
            },
        ]
    )

    caminho_arquivo = tmp_path / "registros_validos.csv"

    # Execução
    salvar_csv_valido(
        df,
        caminho_arquivo,
    )

    # Validação
    assert caminho_arquivo.exists()

    df_salvo = pd.read_csv(caminho_arquivo)

    assert len(df_salvo) == 2
    assert df_salvo.loc[0, "transacao_id"] == "TXN_001"
    assert df_salvo.loc[1, "produto"] == "Tea"


def test_salvar_csv_invalidos_cria_arquivo_com_motivo_erro(
    tmp_path,
):
    # Preparação
    registros_invalidos = [
        {
            "transacao_id": "TXN_003",
            "produto": "Coffee",
            "quantidade": None,
            "preco_unitario": 2.5,
            "valor_total": None,
            "metodo_pagamento": "Cash",
            "localidade": "Takeaway",
            "data_transacao": "2026-07-16",
            "motivo_erro": "Quantidade inválida",
        }
    ]

    caminho_arquivo = tmp_path / "registros_invalidos.csv"

    # Execução
    salvar_csv_invalidos(
        registros_invalidos,
        caminho_arquivo,
    )

    # Validação
    assert caminho_arquivo.exists()

    df_salvo = pd.read_csv(caminho_arquivo)

    assert len(df_salvo) == 1
    assert "motivo_erro" in df_salvo.columns
    assert (
        df_salvo.loc[0, "motivo_erro"]
        == "Quantidade inválida"
    )