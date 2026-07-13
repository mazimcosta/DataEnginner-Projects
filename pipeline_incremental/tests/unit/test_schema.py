import pytest
from src.schema import ProdutoSchema,validar_schema,ValidationError

def test_registro_valido():

    registro={
        'id_venda':1,
        'data_venda':'2026-04-01',
        'id_cliente':2,
        'nome_cliente':'Joao',
        'cidade':'Fortaleza',
        'categoria':'bebidas',
        'produto':'refrigerante',
        'quantidade':5,
        'preco_unitario':2.58,
        'desconto':0.5,
        'status_pagamento':'pago'
    }

    produto=ProdutoSchema(**registro)

    assert produto.id_venda == 1
    assert produto.id_cliente == 2
    assert produto.nome_cliente == 'Joao'

def test_registro_invalido():

    registro={
        'id_venda':-5,
        'data_venda':'2026-04-01',
        'id_cliente':2,
        'nome_cliente':'Joao',
        'cidade':'Fortaleza',
        'categoria':'bebidas',
        'produto':'refrigerante',
        'quantidade':5,
        'preco_unitario':2.58,
        'desconto':0.5,
        'status_pagamento':'pago'
    }

    with pytest.raises(ValidationError):
        ProdutoSchema(**registro)