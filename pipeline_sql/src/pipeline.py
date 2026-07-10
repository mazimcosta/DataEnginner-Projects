
from config.settings import OUTPUT_DIR,INPUT_DIR,SQL_DIR
from src.extractor import extrair_dados
from src.schema import validar_schema
from src.sql_executor import executar_sql
from src.loader import salvar_csv_invalidos,salvar_csv_valido,salvar_banco

def executar_pipeline():

    df_bruto=extrair_dados(INPUT_DIR/'mercado.csv')
    
    df_valido,registros_invalidos=validar_schema(df_bruto)

    salvar_csv_valido(df_valido,OUTPUT_DIR/'registros_validos.csv')

    salvar_csv_invalidos(registros_invalidos,OUTPUT_DIR/'registros_invalidos.csv')

    executar_sql(SQL_DIR/'create_tables.sql')

    executar_sql(SQL_DIR/'clear_tables.sql')

    salvar_banco(df_valido)

    executar_sql(SQL_DIR/'load_tables.sql')

    

   