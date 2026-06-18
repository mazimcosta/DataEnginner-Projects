

# Primeiro pipeline:
import json

import csv
caminho_arquivo="data/raw/Teen_Mental_Health_Dataset.csv"
def extrair_dados(caminho_arquivo:str):

    with open(caminho_arquivo,"r",encoding='utf-8') as arquivo:

        leitor=csv.DictReader(arquivo)
        return list(leitor)
    


def transformar_dados(lista:list):
    qtde_homens=0
    qtde_mulheres=0
    maior_idade=0
    menor_idade=999
    frequencia=0
    soma_idades=0
    total_pessoas=0
    media=0
    plataforma_usadas={"instagram":0,"tiktok":0,"both":0}
    plataforma_vencedora=""
    dados_processados={}

    for dado in lista:


        try:
            idade=int(dado.get('age'))
        except (ValueError,TypeError):
            continue
    
        soma_idades+=idade
        total_pessoas+=1

        if idade>maior_idade:
            maior_idade=idade

        if idade<menor_idade:
            menor_idade = idade

        if dado.get('gender')=='male':
            qtde_homens+=1

        elif dado.get('gender')=='female':
            qtde_mulheres+=1

        if dado['platform_usage'].lower()=='instagram':
            plataforma_usadas['instagram']+=1
        elif dado['platform_usage'].lower()=='tiktok':
            plataforma_usadas['tiktok']+=1
        elif dado['platform_usage'].lower()=='both':
            plataforma_usadas['both']+=1

    for plataforma,votos in plataforma_usadas.items():
        if votos>frequencia:
            frequencia = votos
            plataforma_vencedora= plataforma

    media=round((soma_idades/total_pessoas),2) if total_pessoas>0 else 0
    return {"homens":qtde_homens,
            "mulheres":qtde_mulheres,
            "maior_idade":maior_idade,
            "menor_idade":menor_idade,
            "media":media,
            "plataforma_vencedora":plataforma_vencedora,
            "votos":frequencia}

def carregar_dados(dados:dict):
    with open('data/processed/relatorio.json','w',encoding='utf-8') as arquivo:
        json.dump(dados,arquivo,ensure_ascii=False,indent=4)

if __name__=="__main__":
    dados_brutos=extrair_dados(caminho_arquivo)
    dados_processados=transformar_dados(dados_brutos)
    carregar_dados(dados_processados)
    

