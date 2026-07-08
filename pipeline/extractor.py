import logging
import pandas as pd

def extrair_dados(caminho_arquivo:str):
    logging.info('Iniciando extracao de csv')
    df_vendas = pd.read_csv(caminho_arquivo)
    logging.info('Csv extraido com sucesso')
    return df_vendas