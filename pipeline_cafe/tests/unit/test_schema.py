
import pandas as pd
import pytest
from src.schema import ProdutoSchema,validar_schema,ValidationError


def test_schema_valido():

    venda={
        'transacao_id':'TXN_4587',
        'id_incremental':1457,
        'produto':'cerveja',
        'quantidade':8,
        'preco_unitario':4.50,
        'valor_total':36.0,
        'metodo_pagamento':'cartao',
        'localidade':'Manaus',
        'data_transacao':'2026-04-07'
    }

    produto=ProdutoSchema(**venda)

    assert produto.quantidade == 8
    assert produto.produto == 'cerveja'
    assert produto.localidade == 'Manaus'
    assert produto.id_incremental == 1457

def test_schema_invalido():

    venda={
        'transacao_id':'TXN_4587',
        'id_incremental':1457,
        'produto':'cerveja',
        'quantidade':None,
        'preco_unitario':4.50,
        'valor_total':36.0,
        'metodo_pagamento':'cartao',
        'localidade':'Manaus',
        'data_transacao':'2026-04-07'
    }

    with pytest.raises(ValidationError):
        ProdutoSchema(**venda)


def test_registro_valido():
    venda={
        'transacao_id':'TXN_4587',
        'id_incremental':1457,
        'produto':'cerveja',
        'quantidade':8,
        'preco_unitario':4.50,
        'valor_total':36.0,
        'metodo_pagamento':'cartao',
        'localidade':'Manaus',
        'data_transacao':'2026-04-07'
    }
    df=pd.DataFrame([venda])

    df_valido,registros_invalidos=validar_schema(df)

    assert len(df_valido) == 1
    assert len(registros_invalidos) == 0

def test_registro_invalido():

    venda={
        'transacao_id':'TXN_4587',
        'id_incremental':1457,
        'produto':'cerveja',
        'quantidade':None,
        'preco_unitario':4.50,
        'valor_total':36.0,
        'metodo_pagamento':'cartao',
        'localidade':'Manaus',
        'data_transacao':'2026-04-07'
    }
    df=pd.DataFrame([venda])
    df_valido,registros_invalidos=validar_schema(df)

    assert len(df_valido) == 0
    assert len(registros_invalidos) == 1