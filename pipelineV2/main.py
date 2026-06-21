
from pipeline_research_mental.extract import extrair_dados
from pipeline_research_mental.transform import processar_dados
from pipeline_research_mental.load import gerar_csv,gerar_relatorio
from pipeline_research_mental.schema import validar_schema

if __name__=='__main__':

        try:
                dados_brutos,colunas_arquivo=extrair_dados('input/invalido.csv')
        except FileNotFoundError :
                print('Arquivo nao encontrado')
        else:
                validar_schema(colunas_arquivo)
                        
                clientes_validos,clientes_invalidos,relatorio=processar_dados(dados_brutos)

                gerar_csv(clientes_validos,'output/clientes_validos.csv')

                gerar_relatorio(relatorio,'output/relatorio.json')