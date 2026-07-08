import pandas as pd
import logging
from schema import VendaSchema
from pydantic import ValidationError

def validar_schema(df:pd.DataFrame):
    logging.info('Iniciando validacao de dados')
    registros_validos=[]
    registros_invalidos=[]

    for registro in df.to_dict('records'):

        try:
            venda=VendaSchema(**registro)
            registros_validos.append(venda.model_dump())
        except ValidationError as error:
            registros_invalidos.append(registro)
            logging.error(f'Erro de validacao{error}')

    df_limpo =pd.DataFrame(registros_validos)
    logging.info(f' Validacao executada com sucesso. Sao `{len(registros_validos)} validos e {len(registros_invalidos)} invalidos.')

    return df_limpo,registros_invalidos

