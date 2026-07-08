
import pandas as pd

def limpar_valor_frete(valor):
    if pd.isna(valor):
        return None
    
    
    valor = str(valor).replace('R$','').strip()
    
    
    if '.' in valor and ',' in valor:
        valor= valor.replace('.','')
        valor=valor.replace(',','.')

    if '.' in valor:
        pass
    else:
        pass

    return valor

def remover_invalidos(df:pd.DataFrame):
    df = df.dropna(subset=['id_entrega','peso_kg','valor_frete','data_entrega','status_entrega'])
    df = df[(df['peso_kg']>0) & (df['valor_frete']>0)]
    return df


def converter_float(df:pd.DataFrame):
    df['valor_frete'] = pd.to_numeric(df['valor_frete'],errors='coerce')
    return df

def tratar_nulos(df:pd.DataFrame):
    df = df.fillna({
        'motorista':'Nao informado',
        'cidade':'Nao informada',
        'filial':'Nao informada'
    })
    return df

def limpar_motorista(nome):
    
    correcoes={'C-srlos':'Carlos','Ana-':'Ana','Patr-icia':'Patricia'}

    nome=str(nome).replace(',','').strip()
    nome= nome.replace('.','')
    nome = nome.lower().title()

    return correcoes.get(nome,nome)


def limpar_texto(nome):
    nome=str(nome).strip()
    nome=nome.replace(',','')
    nome= nome.replace('.','')
    nome = nome.lower().title()

    return nome

def criar_colunas(df:pd.DataFrame):
    df['valor_por_kg'] = df['valor_frete']/df['peso_kg']
    return df


def processar_dados(df:pd.DataFrame):
    df=tratar_nulos(df)
    df['valor_frete'] = df['valor_frete'].apply(limpar_valor_frete)
    df = converter_float(df)
    df = remover_invalidos(df)
    df['motorista'] = df['motorista'].apply(limpar_motorista)
    df['filial'] = df['filial'].apply(limpar_texto)
    df['cidade']=df['cidade'].apply(limpar_texto)
    df['status_entrega'] = df['status_entrega'].apply(limpar_texto)
    df_limpo = criar_colunas(df)
    return df_limpo



