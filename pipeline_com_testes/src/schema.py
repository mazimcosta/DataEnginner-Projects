
import pandas as pd
from pydantic import(BaseModel,Field,ValidationError)
from src.logger import logger


class PedidoSchema(BaseModel):
    id_pedido:int=Field(gt=0)
    mesa:int=Field(gt=0)
    item:str=Field(min_length=3)
    categoria:str=Field(min_length=3)
    quantidade:int=Field(gt=0)
    preco_unitario:str=Field(min_length=2)
    status:str=Field(min_length=4)
    pagamento:str=Field(min_length=3)


def validar_schema(df:pd.DataFrame):
    registros_validos=[]
    registros_invalidos=[]
    logger.info('Iniciando validacao de dados')
    for registro in df.to_dict('records'):
        try:
            pedido=PedidoSchema(**registro)
            registros_validos.append(pedido.model_dump())

        except ValidationError as error:
            registros_invalidos.append(registro)
            logger.info(f' Erro de validacao:{error}')
    
    logger.info(f'Dados validados com sucesso. Sao {len(registros_validos)} validos e {len(registros_invalidos)} invalidos.')
    df_valido=pd.DataFrame(registros_validos)
    return df_valido,registros_invalidos