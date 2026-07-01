
import pandas as pd

def extrair_dados(caminho_arquivo:str):

    df_vendas = pd.read_csv(caminho_arquivo)

    return df_vendas