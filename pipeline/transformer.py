import pandas as pd

def limpar_preco(valor):
    valor = str(valor).replace('R$','').strip()

    if ',' in valor and '.' in valor:
        valor = valor.replace('.','')
        valor = valor.replace(',','.')

    elif '.' in valor:
        pass
    else:
        pass
    return valor

def limpar_texto(nome):
    nome=str(nome).strip()
    nome = nome.lower().title()

    return nome

def limpar_vendedor(nome):
    correcoes ={'Csrlos':'Carlos'}

    
    nome=str(nome).strip()
    nome=nome.replace(',','')
    nome = nome.replace(';','')
    nome=nome.lower().title()
    return correcoes.get(nome,nome)

def tratar_nulos(df:pd.DataFrame):
    df = df.fillna({
        'desconto':0,
        'filial':'Nao informado',
        'vendedor':'Venda online'
    })
    return df

def remover_invalidos(df:pd.DataFrame):
    

    df["preco_unitario"] = pd.to_numeric(
        df["preco_unitario"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["quantidade", "preco_unitario"]
    )

    return df

def criar_valor_total(df:pd.DataFrame):
    df['valor_total'] = df['quantidade'] * df['preco_unitario'] - df['desconto']
    return df


def processar_dados(df:pd.DataFrame):
    df =tratar_nulos(df)
    df['preco_unitario'] = df['preco_unitario'].apply(limpar_preco)
    df =remover_invalidos(df)
    df['filial'] = df['filial'].apply(limpar_texto)
    df['categoria'] = df['categoria'].apply(limpar_texto)
    df['vendedor'] = df['vendedor'].apply(limpar_vendedor)
    df =criar_valor_total(df)

    return df