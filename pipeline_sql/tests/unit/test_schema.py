import pandas as pd
from src.schema import VendaSchema,validar_schema,ValidationError
import pytest

def test_registro_valido():
    venda={
        'id_venda':1,
        'data_venda':'2026-07-02',
        'id_cliente':4,
        'nome_cliente':'Marcos',
        'cidade':'Maracanau',
        'categoria':'bebidas',
        'produto':'refrigerante',
        'quantidade':4,
        'preco_unitario':12.50,
        'desconto':1.50,
        'status_pagamento':'pago'

    }
    
    item=VendaSchema(**venda)

    assert item.id_venda==1
    assert item.nome_cliente =='Marcos'
    assert item.quantidade==4
    assert item.categoria=='bebidas'

def test_registro_invalido():

    venda1={
        'id_venda':-1,
        'data_venda':'2026-07-02',
        'id_cliente':None,
        'nome_cliente':'Marta',
        'cidade':'Fortaleza',
        'categoria':'bebidas',
        'produto':'suco',
        'quantidade':-20,
        'preco_unitario':85.50,
        'desconto':4.50,
        'status_pagamento':'pago'
    }   

    with pytest.raises(ValidationError):
        VendaSchema(**venda1)