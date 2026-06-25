
from extract_api import extrair_dados_API
from transform import processar_dados_API
from load import(gerar_csv_validos,gerar_csv_invalidos,gerar_relatorio)

def executar_pipeline():
    try:
        dados =extrair_dados_API('https://fakestoreapi.com/products')

        produtos_validos,produtos_invalidos,relatorio = processar_dados_API(dados)

        gerar_csv_validos(produtos_validos,'output/produtos_validos.csv')

        gerar_csv_invalidos(produtos_invalidos,'output/produtos_invalidos.csv')

        gerar_relatorio(relatorio,'output/relatorio.json')

    except (FileNotFoundError,ValueError) as error:
        print(error)

if __name__ == '__main__':
    executar_pipeline()