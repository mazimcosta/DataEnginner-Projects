
import csv
import json

def gerar_csv_validos(usuarios_validos:list,caminho_arquivo:str):

    campos=['usuario_id','nome','email']
    with open(caminho_arquivo,'w',encoding='utf-8',newline="") as arquivo:
        escritor = csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for usuario in usuarios_validos:
            escritor.writerow(usuario)


def gerar_csv_invalidos(usuarios_invalidos:list,caminho_arquivo:str):

    campos= ['usuario_id','nome','email','erro']

    with open(caminho_arquivo,'w',encoding='utf-8',newline="") as arquivo:
        escritor = csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for usuario in usuarios_invalidos:
            escritor.writerow(usuario)


def gerar_relatorio(relatorio:dict,caminho_arquivo:str):

    with open(caminho_arquivo,'w',encoding='utf-8') as arquivo:
        json.dump(relatorio,arquivo,ensure_ascii=False, indent=4)

