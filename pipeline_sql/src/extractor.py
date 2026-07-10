
import pandas as pd
from src.logger import logger


def extrair_dados(caminho_arquivo:str):
    logger.info('Iniciando extracao de dados')
    
    df=pd.read_csv(caminho_arquivo)
    logger.info('Dados extraidos com sucesso')
    return df