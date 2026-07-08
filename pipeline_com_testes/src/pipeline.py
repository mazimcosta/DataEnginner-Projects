
from src.extractor import extrair_dados
from src.transformer import processar_dados
from src.schema import validar_schema
from loader import(salvar_banco,salvar_csv_valido,salvar_csv_invalido)
from config.settings import OUTPUT_DIR,INPUT_DIR


def executar_pipeline():

    df_bruto=extrair_dados(INPUT_DIR/'restaurante.csv')

    df_valido,registros_invalidos=validar_schema(df_bruto)

    df_limpo=processar_dados(df_valido)

    salvar_csv_valido(df_limpo,OUTPUT_DIR/'pedidos_validos.csv')

    salvar_csv_invalido(registros_invalidos,OUTPUT_DIR/'pedidos_invalidos.csv')

    salvar_banco(df_limpo)