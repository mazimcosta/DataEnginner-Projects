import pandas as pd
from pydantic import (BaseModel,Field,ValidationError)
from src.logger import logger
from datetime import date

class ProdutoSchema(BaseModel):
    
    transacao_id:str=Field(min_length=3)
    id_incremental:int=Field(gt=0)
    produto:str=Field(min_length=3)
    quantidade:int=Field(gt=0)
    preco_unitario:float=Field(gt=0)
    valor_total:float=Field(gt=0)
    metodo_pagamento:str=Field(min_length=3)
    localidade:str=Field(min_length=3)
    data_transacao:date


def validar_schema(df:pd.DataFrame):
    registros_validos=[]
    registros_invalidos=[]

    logger.info('Iniciando validacao de dados.')

    for registro in df.to_dict('records'):
        registro_normalizado={campo:None if pd.isna(valor) else valor for campo,valor in registro.items()}

        try:
            produto=ProdutoSchema(**registro_normalizado)
            registros_validos.append(produto.model_dump())

        except ValidationError as error:
            registros_invalidos.append({**registro_normalizado,'motivo_erro':str(error)})
            

        except Exception as error:
            print(error)
            raise
    
    logger.info(f'Validacao de dados concluida. foram {len(registros_validos)} validos e {len(registros_invalidos)} invalidos')
    df_valido=pd.DataFrame(registros_validos)

    return df_valido,registros_invalidos