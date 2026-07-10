
import pandas as pd
from src.logger import logger
from pydantic import(BaseModel,ValidationError,Field)
from datetime import date

class  VendaSchema(BaseModel):
    id_venda:int=Field(gt=0)
    data_venda:date
    id_cliente:int=Field(gt=0)
    nome_cliente:str=Field(min_length=3)
    cidade:str=Field(min_length=3)
    categoria:str=Field(min_length=3)
    produto:str=Field(min_length=3)
    quantidade:int=Field(gt=0)
    preco_unitario:float=Field(gt=0)
    desconto:float
    status_pagamento:str=Field(min_length=3)




def validar_schema(df:pd.DataFrame):
    logger.info('Iniciando validacao de dados')

    registros_validos=[]
    registros_invalidos=[]
    for registro in df.to_dict('records'):
        try:
            venda=VendaSchema(**registro)
            registros_validos.append(venda.model_dump())
        except ValidationError as error:
            registros_invalidos.append(registro)
            logger.error(f'Erro de validacao:{error}')

    logger.info(f'Validacao de dados concluida. Sao {len(registros_validos)} validos e {len(registros_invalidos)} registros invalidos.')
    df_valido=pd.DataFrame(registros_validos)

    return df_valido,registros_invalidos


