
from extractor import extrair_dados
from transformer import processar_dados
from loader import salvar_csv,salvar_banco

def executar_pipeline():
    try:
            
        df_bruto = extrair_dados('vendas_sujas.csv')

        df_limpo =processar_dados(df_bruto)

        salvar_csv(df_limpo,'output/vendas.csv')

        salvar_banco(df_limpo)

    except(FileNotFoundError,ValueError) as error:
        print(error)