import logging
from extractor import extrair_dados
from transformer import processar_dados
from loader import salvar_csv,salvar_banco,salvar_invalidos
from schema import validar_schema

def executar_pipeline():
    try:
            
        df_bruto = extrair_dados('vendas_sujas.csv')

        df_limpo,registros_invalidos= validar_schema(df_bruto)


        df_limpo =processar_dados(df_limpo)

        salvar_csv(df_limpo,'output/vendas.csv')

        salvar_invalidos(registros_invalidos,'invalidos.csv')

        salvar_banco(df_limpo)

    except(FileNotFoundError,ValueError) as error:
        logging.error(f'Falha na execucao do pipeline: {error}')