
import csv
import json

def gerar_csv(vendas_validas,saida_arquivo):
    
    campos=['produto','preco','quantidade','categoria','faturamento']

    with open(saida_arquivo,'w',encoding='utf-8') as arquivo:

        escritor=csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for venda in vendas_validas:
            escritor.writerow(venda)


def gerar_relatorio(relatorio,saida_arquivo):

    with open(saida_arquivo,'w',encoding='utf-8') as arquivo:
        json.dump(relatorio,arquivo,ensure_ascii=False,indent=4)
        