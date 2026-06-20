

# Primeiro pipeline:
import json
import psycopg2
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

def carrgar_banco(dados):
    lista=[]
    
     
    

    for dado in dados:
        try:
            idade=int(dado.get('age'))
        except:
            continue
        
        genero=dado.get('gender')
        plataforma=dado.get('platform_usage')
        lista.append((idade,genero,plataforma))

    query=("""INSERT INTO raw_mental_health (idade,genero,plataforma) VALUES (%s,%s,%s) """)

    try:
        conexao=psycopg2.connect(
        dbname="banco",
        user="postgres",
        password="senha",
        host="localhost",
        port="5432"
        )
        cursor=conexao.cursor()
        
        cursor.executemany(query,lista)
        conexao.commit()
    
    except Exception as error:
        if 'conexao' in locals():
            conexao.rollback()
            print(f'Erro falha na insercao:{error}')
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()
        print('Conexao encerrada')






if __name__=="__main__":
    dados_brutos=extrair_dados(caminho_arquivo)
    dados_processados=transformar_dados(dados_brutos)
    carregar_dados(dados_processados)
    carrgar_banco(dados_brutos)   

