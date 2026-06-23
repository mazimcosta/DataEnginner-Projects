import csv
import json

def gerar_csv(funcionarios_validos,caminho_arquivo):
    campos=['nome','email','salario','departamento','faixa_salarial']

    with open(caminho_arquivo,'w',encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for funcionario in funcionarios_validos:
            escritor.writerow(funcionario)


def gerar_relatorio(relatorio,caminho_arquivo):

    with open(caminho_arquivo,'w',encoding='utf-8') as arquivo:
        json.dump(relatorio,arquivo,ensure_ascii=False, indent=4)


def gerar_csv_invalidos(funcionarios_invalidos:list,caminho_arquivo):

    lista=[]
    for func in funcionarios_invalidos:
        funcionario=func.get('funcionario')
        erro = func.get('erro')

        lista.append(
            {'nome':funcionario['nome'],
             'email':funcionario['email'],
             'salario':funcionario['salario'],
             'departamento':funcionario['departamento'],
             'erro':erro
        }
        )
    campos=['nome','email','salario','departamento','erro']

    with open(caminho_arquivo,'w',encoding='utf-8') as arquivo:
        escritor=csv.DictWriter(arquivo,fieldnames=campos)
        escritor.writeheader()
        for funcionario in lista:
            escritor.writerow(funcionario)
    
        