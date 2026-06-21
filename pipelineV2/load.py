import json
import csv


def gerar_csv(clientes_validos,saida_arquivo:str):

    campos=['nome','idade','genero']

    with open(saida_arquivo,'w') as arquivo:
        escritor=csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for cliente in clientes_validos:
            escritor.writerow(cliente)


def gerar_relatorio(relatorio,arquivo_saida):

    with open(arquivo_saida,'w',encoding='utf-8') as arquivo:
        json.dump(relatorio,arquivo,ensure_ascii=False,indent=4)
