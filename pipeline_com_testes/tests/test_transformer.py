
import pytest
import pandas as pd
from src.transformer import limpar_preco_unitario,converter_preco_unitario,limpar_status,limpar_texto,remover_invalidos

def  test_limpar_preco_unitario_com_virgula():

    

    resultado=limpar_preco_unitario('12,90')

    assert resultado=='12.90'

def  test_limpar_preco_unitario_com_ponto_decimal():

    resultado=limpar_preco_unitario('45.90')

    assert resultado == '45.90'

def  test_limpar_preco_unitario_com_none():
    resultado=limpar_preco_unitario(None)

    assert resultado == None

def test_converter_preco_unitario_com_texto_invalido():
    df=pd.DataFrame({'preco_unitario':['abc','25.90']})

    resultado=converter_preco_unitario(df)

    assert pd.isna(resultado.loc[0,'preco_unitario'])


def  test_limpar_status_valido_pago():
    resultado=limpar_status('pago')

    assert resultado=='pago'

def test_limpar_status_valido_cancelado():
    resultado=limpar_status('CANCELADO')

    assert resultado == 'cancelado'

def  test_limpar_status_invalido():
    resultado=limpar_status('pendente')
    assert resultado ==None

def test_limpar_texto_padroniza():
    resultado = limpar_texto('pizza calabresa')
    assert resultado == 'Pizza Calabresa'

def   test_limpar_texto_com_none():
    resultado=limpar_texto(None)

    assert resultado == None

def test_remover_invalidos_remove_linhas_com_nulos():
    pedido={
        'id_pedido':1,
        'mesa':5,
        'item':'bebida',
        'categoria':'bebidas',
        'quantidade':2,
        'preco_unitario':45.90,
        'status':'pago',
        'pagamento':'cartao'
    }
    pedido1={
        'id_pedido':2,
        'mesa':None,
        'item':'comida',
        'categoria':'pratos',
        'quantidade':3,
        'preco_unitario':95.90,
        'status':'pago',
        'pagamento':'cartao'
    }
    pedido2={
        'id_pedido':3,
        'mesa':8,
        'item':None,
        'categoria':'bebidas',
        'quantidade':7,
        'preco_unitario':125.90,
        'status':'pago',
        'pagamento':'cartao'
    }
    df=pd.DataFrame([pedido,pedido1,pedido2])
    resultado=remover_invalidos(df)

    assert len(resultado)==1


