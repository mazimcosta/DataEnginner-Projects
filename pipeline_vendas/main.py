
from extract import extrair_dados
from transform import processar_dados
from load import gerar_csv,gerar_relatorio
from schema import validar_schema




if __name__=='__main__':


    try:
        dados_brutos,colunas_arquivo=extrair_dados('input/vendas.csv')
        
        validar_schema(colunas_arquivo)

        vendas_validas,vendas_invalidas,relatorio=processar_dados(dados_brutos)

        gerar_csv(vendas_validas,'output/vendas_validas.csv')

        gerar_relatorio(relatorio,'output/relatorio.json')

    except (FileNotFoundError,ValueError) as error:
        print(error)


