
import csv
import json

def gerar_csv_validos(produtos_validos:list,caminho_arquivo:str):
    campos= ['produto_id','nome','preco','descricao','categoria','classificacao']

    with open(caminho_arquivo,'w',newline="",encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for produto in produtos_validos:
            escritor.writerow(produto)


def gerar_csv_invalidos(produtos_invaidos:list,caminho_arquivo:str):
    campos= ['produto_id','nome','preco','descricao','erro']

    with open(caminho_arquivo,'w',newline="",encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for produto in produtos_invaidos:
            escritor.writerow(produto)

def gerar_relatorio(relatorio:dict,caminho_arquivo:str):

    with open(caminho_arquivo,'w',encoding='utf-8') as arquivo:
        json.dump(relatorio,arquivo,ensure_ascii=False, indent=4)
