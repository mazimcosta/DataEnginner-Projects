
import pandas as pd
from src.logger import logger
from pydantic import(BaseModel,Field,ValidationError)
from datetime import date

class ProdutoSchema(BaseModel):
    id_venda:int=Field(gt=0)
    data_venda:date
    id_cliente:int=Field(gt=0)
    nome_cliente:str=Field(min_length=3)
    cidade:str=Field(min_length=3)
    categoria:str=Field(min_length=3)
    produto:str=Field(min_length=3)
    quantidade:int
    preco_unitario:float
    desconto:float
    status_pagamento:str=Field(min_length=3)

def validar_schema(df:pd.DataFrame):
    logger.info('Iniciando validacao de dados')
    registros_validos=[]
    registros_invalidos=[]

    for registro in df.to_dict('records'):
        try:
            produto=ProdutoSchema(**registro)
            registros_validos.append(produto.model_dump())
        except ValidationError as error:
            registros_invalidos.append(registro)
            logger.info(f'Falha na validacao:{error}')

    logger.info(f'Validacao de dados concluida com sucesso. Foram {len(registros_validos)} validos e {len(registros_invalidos)} invalidos')

    df=pd.DataFrame(registros_validos)
    return df,registros_invalidos

