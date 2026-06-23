
from extract import extrair_dados
from schema import validar_schema
from transform import processar_dados
from load import gerar_csv,gerar_relatorio,gerar_csv_invalidos

def executar_pipeline():

    try:
        dados_brutos,colunas_arquivo = extrair_dados('input/funcionários.csv')

        validar_schema(colunas_arquivo)

        funcionarios_validos,funcionarios_invalidos,relatorio = processar_dados(dados_brutos)

        gerar_csv(funcionarios_validos,'output/funcionarios_validos.csv')

        gerar_relatorio(relatorio,'output/relatorio.json')

        gerar_csv_invalidos(funcionarios_invalidos,'output/funcionarios_invalidos.csv')

    except (FileNotFoundError,ValueError) as error:
        print(error)

if __name__=='__main__':
    executar_pipeline()
