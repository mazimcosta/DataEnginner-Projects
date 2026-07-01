# %%
import pandas as pd
from extractor import extrair_dados
df =extrair_dados('vendas_sujas.csv')


# %%
#Verificando nulos
df.isna().sum()


#Eliminando nulos de colunas obrigatorias
df.dropna(subset='quantidade',inplace=True)

#Preenchendo colunas opcionais com valores da regra de negocio
df =df.fillna({
    'filial':'Nao informado',
    'desconto':0,
    'vendedor':'Vendas online'
})

# %%
#Tratando coluna preco_unitario:
df['preco_unitario'] = df['preco_unitario'].astype(str).str.replace('.','',regex=False)



# %%
df['preco_unitario'] = df['preco_unitario'].astype(str).str.replace(',','.',regex=False)

# %%
df['preco_unitario'] = df['preco_unitario'].astype(str).str.replace('R$','', regex=False).str.strip()


# %%
#Convertendo para numeros
df['preco_unitario'] = pd.to_numeric(df['preco_unitario'],errors='coerce')

# %%
#Eliminando linha com preco unitario que era texto e ficou NaN
df.dropna(subset='preco_unitario',inplace=True)

# %%
#Criando a coluna valor_total
df['valor_total'] = (df['quantidade'] *df['preco_unitario']) - df['desconto']
display(df)

# %%
# Tratando filial e categoria:
df[['filial','categoria']] = df[['filial','categoria']].astype(str).map(lambda nome:nome.lower().title())

# %%
#Agora tratando a coluna vendedor

df['vendedor'] = df['vendedor'].astype(str).str.replace(',','',regex=False).str.replace(';','',regex=False).str.lower().str.capitalize()

# %%
correcoes = {'Csrlos':'Carlos'}
df['vendedor'] = df['vendedor'].replace(correcoes)

# %%
display(df)


