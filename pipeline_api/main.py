
from extract_api import extrair_dados_api
from transform import processar_dados
from load import(gerar_csv_invalidos,gerar_csv_validos,gerar_relatorio)

def executar_pipeline():

    try:
        dados = extrair_dados_api('https://jsonplaceholder.typicode.com/users')

        usuarios_validos,usuarios_invalidos,relatorio = processar_dados(dados)

        gerar_csv_validos(usuarios_validos,'output/usuarios_validos.csv')

        gerar_csv_invalidos(usuarios_invalidos,'output/usuarios_invalidos.csv')

        gerar_relatorio(relatorio,'output/relatorio.json')

    except (FileNotFoundError,ValueError) as error:
        print(error)


if __name__ == '__main__':
    executar_pipeline()