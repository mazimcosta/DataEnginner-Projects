import pandas as pd

from src.transformer import (
    converter_valor_numerico,
    limpar_texto,
)


def test_converter_valor_numerico():
    venda = {
        "quantidade": ["UNKNOWN", 4, 5, 8],
        "preco_unitario": ["ERROR", 4, 8, 7],
        "valor_total": ["INVALIDO", 16, 40, 56],
    }

    df = pd.DataFrame(venda)

    resultado = converter_valor_numerico(df)

    assert pd.isna(resultado.loc[0, "quantidade"])
    assert pd.isna(resultado.loc[0, "preco_unitario"])
    assert pd.isna(resultado.loc[0, "valor_total"])

    assert resultado.loc[1, "quantidade"] == 4
    assert resultado.loc[2, "quantidade"] == 5
    assert resultado.loc[3, "quantidade"] == 8

    assert resultado.loc[1, "preco_unitario"] == 4
    assert resultado.loc[1, "valor_total"] == 16


def test_limpar_texto():
    assert limpar_texto("tea") == "Tea"
    assert limpar_texto(" sugar ") == "Sugar"
    assert limpar_texto("MILK") == "Milk"
    assert limpar_texto(pd.NA) is None