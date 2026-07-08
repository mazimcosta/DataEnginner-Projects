
import pandas as pd
from src.logger import logger

def limpar_preco_unitario(valor):
    
    if pd.isna(valor):
        return None
    
    valor=str(valor).strip()
    if ',' in valor and '.' in valor:
        valor=valor.replace('.','')
        valor=valor.replace(',','.')

    if ',' in valor:
        valor=valor.replace(',','.')
        
    if '.' in valor:
        pass

    return valor


def converter_preco_unitario(df:pd.DataFrame):
    df['preco_unitario'] = pd.to_numeric(df['preco_unitario'],errors='coerce')

    return df



def limpar_status(nome):

    if pd.isna(nome):
        return None
    
    nome=str(nome).lower().strip()
    if nome not in ['pago','cancelado']:
        return None
    
    return nome

def limpar_texto(nome):
    if pd.isna(nome):
        return None
    
    nome=str(nome).title().strip()
    return nome

def remover_invalidos(df:pd.DataFrame):
    df=df.dropna(subset=df.columns)

    return df

def calcular_valor_total(df:pd.DataFrame):
    df['valor_total']=(df['quantidade'] * df['preco_unitario']).round(2)
    return df


def processar_dados(df:pd.DataFrame):
    logger.info('Iniciando tratamento de dados')
    df['preco_unitario']=df['preco_unitario'].apply(limpar_preco_unitario)
    df=converter_preco_unitario(df)
    df['status']=df['status'].apply(limpar_status)
    df['item']=df['item'].apply(limpar_texto)
    df['categoria']=df['categoria'].apply(limpar_texto)
    df['pagamento'] = df['pagamento'].apply(limpar_texto)
    df=remover_invalidos(df)
    df=calcular_valor_total(df)
    logger.info('Tratamento de dados concluido')

    return df