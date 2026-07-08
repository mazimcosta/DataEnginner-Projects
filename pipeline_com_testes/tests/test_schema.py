
import pandas as pd
from src.schema import PedidoSchema,validar_schema,ValidationError
import pytest


def  test_pedido_schema_valido():

    item={
        'id_pedido':1,
        'mesa':5,
        'item':'bebida',
        'categoria':'bebidas',
        'quantidade':2,
        'preco_unitario':'45.90',
        'status':'pago',
        'pagamento':'cartao'
    }

    pedido=PedidoSchema(**item)

    assert pedido.id_pedido ==1
    assert pedido.mesa ==5
    assert pedido.item =='bebida'
    assert pedido.categoria =='bebidas'
    assert pedido.quantidade == 2
    assert pedido.status == 'pago'
    assert pedido.pagamento =='cartao'


def  test_pedido_schema_id_invalido():
    item={
        'id_pedido':-1,
        'mesa':5,
        'item':'bebida',
        'categoria':'bebidas',
        'quantidade':2,
        'preco_unitario':'45.90',
        'status':'pago',
        'pagamento':'cartao'
    }

    with pytest.raises(ValidationError):
        pedido=PedidoSchema(**item)


def  test_pedido_schema_mesa_invalida():
    item={
        'id_pedido':1,
        'mesa':-1,
        'item':'bebida',
        'categoria':'bebidas',
        'quantidade':2,
        'preco_unitario':'45.90',
        'status':'pago',
        'pagamento':'cartao'
    }

    with pytest.raises(ValidationError):
        pedido=PedidoSchema(**item)


def test_pedido_schema_item_curto():
    item={
        'id_pedido':1,
        'mesa':5,
        'item':'be',
        'categoria':'bebidas',
        'quantidade':2,
        'preco_unitario':'45.90',
        'status':'pago',
        'pagamento':'cartao'
    }

    with pytest.raises(ValidationError):
        pedido=PedidoSchema(**item)

def  test_pedido_schema_categoria_curta():
    item={
        'id_pedido':1,
        'mesa':5,
        'item':'bebida',
        'categoria':'be',
        'quantidade':2,
        'preco_unitario':'45.90',
        'status':'pago',
        'pagamento':'cartao'
    }

    with pytest.raises(ValidationError):
        pedido=PedidoSchema(**item)


def  test_pedido_schema_quantidade_invalida():
    item={
        'id_pedido':1,
        'mesa':5,
        'item':'bebida',
        'categoria':'bebida',
        'quantidade':-1,
        'preco_unitario':'45.90',
        'status':'pago',
        'pagamento':'cartao'
    }
    with pytest.raises(ValidationError):
        pedido=PedidoSchema(**item)

def  test_pedido_schema_preco_unitario_nulo():
    item={
        'id_pedido':1,
        'mesa':5,
        'item':'bebida',
        'categoria':'bebida',
        'quantidade':2,
        'preco_unitario':None,
        'status':'pago',
        'pagamento':'cartao'
    }
    with pytest.raises(ValidationError):
        pedido=PedidoSchema(**item)

def  test_pedido_schema_pagamento_nulo():
    item={
        'id_pedido':1,
        'mesa':5,
        'item':'bebida',
        'categoria':'bebida',
        'quantidade':2,
        'preco_unitario':'45.00',
        'status':'pago',
        'pagamento':None
    }
    with pytest.raises(ValidationError):
        pedido=PedidoSchema(**item)

def  test_validar_schema_dataframe_totalmente_valido():
    item={
        'id_pedido':1,
        'mesa':5,
        'item':'bebida',
        'categoria':'bebida',
        'quantidade':2,
        'preco_unitario':'74.95',
        'status':'pago',
        'pagamento':'cartao'
    }
    item1={
        'id_pedido':2,
        'mesa':3,
        'item':'sobremesa',
        'categoria':'prato principal',
        'quantidade':2,
        'preco_unitario':'85.24',
        'status':'pago',
        'pagamento':'cartao'
    }

    df=pd.DataFrame([item,item1])
    df_valido,registros_invalidos=validar_schema(df)

    assert len(df_valido)==2
    assert len(registros_invalidos)==0

def test_validar_schema_dataframe_misto():
    item={
        'id_pedido':1,
        'mesa':5,
        'item':'bebida',
        'categoria':'bebida',
        'quantidade':2,
        'preco_unitario':'74.95',
        'status':'pago',
        'pagamento':'cartao'
    }
    item1={
        'id_pedido':-7,
        'mesa':None,
        'item':'so',
        'categoria':'prato principal',
        'quantidade':2,
        'preco_unitario':'85.24',
        'status':'pago',
        'pagamento':'cartao'
    }

    df=pd.DataFrame([item,item1])
    df_valido,registros_invalidos=validar_schema(df)

    assert len(df_valido)==1
    assert len(registros_invalidos) == 1    