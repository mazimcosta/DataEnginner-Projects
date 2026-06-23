

import csv

def extrair_dados(caminho_arquivo):

    with open(caminho_arquivo,'r',encoding='utf-8') as arquivo:
        dados_brutos=csv.DictReader(arquivo)
        colunas_arquivo=dados_brutos.fieldnames
        return list(dados_brutos),colunas_arquivo
    
    