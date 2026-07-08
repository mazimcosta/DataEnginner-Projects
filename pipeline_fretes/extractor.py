
import pandas as pd

def extrair_dados(caminho_arquivo:str):

    df = pd.read_csv(caminho_arquivo)
    return df