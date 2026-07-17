
import pandas as pd
from src.logger import logger

def renomear_colunas(df:pd.DataFrame) -> pd.DataFrame:

    df=df.rename(columns={
        'Transaction ID':'transacao_id',
        'Item':'produto',
        'Quantity':'quantidade',
        'Price Per Unit':'preco_unitario',
        'Total Spent':'valor_total',
        'Payment Method':'metodo_pagamento',
        'Location':'localidade',
        'Transaction Date':'data_transacao'
    })
    return df


def converter_valor_numerico(df:pd.DataFrame) -> pd.DataFrame:

    coluna_numerica = ['preco_unitario','quantidade','valor_total']
    
    for coluna in coluna_numerica:
        df[coluna] = pd.to_numeric(df[coluna],errors='coerce')

    return df

def converter_data(df:pd.DataFrame) -> pd.DataFrame:

    df['data_transacao']=pd.to_datetime(df['data_transacao'],errors='coerce').dt.date

    return df

def limpar_campos_invalidos(df:pd.DataFrame) -> pd.DataFrame:

    colunas_texto=['produto','metodo_pagamento','localidade']

    for coluna in colunas_texto:
        df[coluna]=df[coluna].replace({'ERROR':pd.NA,'UNKNOWN':pd.NA})

    return df

def limpar_texto(nome):

    if pd.isna(nome):
        return None
    nome=str(nome).strip()
    nome=nome.title()
    return nome

def criar_id_incremental(df:pd.DataFrame) ->pd.DataFrame:

    df['id_incremental'] = df['transacao_id'].str.replace('TXN_',"",regex=False)

    df['id_incremental']= pd.to_numeric(df['id_incremental'],errors="coerce")

    return df

def transformar_dados(df:pd.DataFrame) -> pd.DataFrame:

    logger.info('Iniciando limpeza de dados')

    df=renomear_colunas(df)

    df=limpar_campos_invalidos(df)

    df=converter_valor_numerico(df)


    df=converter_data(df)
    
    colunas_texto=['produto','metodo_pagamento','localidade']

    for coluna in colunas_texto:
        df[coluna] = df[coluna].apply(limpar_texto)

    df=criar_id_incremental(df)

    logger.info('Limpeza finalizada com sucesso')


    return df