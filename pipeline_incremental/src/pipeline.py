from config.settings import INPUT_DIR,OUTPUT_DIR,SQL_DIR
from src.extractor import extrair_dados
from src.schema import validar_schema
from src.loader import (salvar_banco,salvar_csv_invalido,salvar_csv_valido)
from src.sql_executor import executar_sql
from src.pipeline_control import buscar_ultimo_id,filtrar_registros,registrar_ultimo_id,obter_maior_id
from src.logger import logger

def executar_pipeline():
    df_bruto=extrair_dados(INPUT_DIR/'farmacia_1.csv')

    df_valido,registros_invalidos=validar_schema(df_bruto)

    executar_sql(SQL_DIR/'criar_tabelas.sql')
        
    ultimo_id=buscar_ultimo_id('pipeline_incremental')

    df_filtrado=filtrar_registros(df_valido,ultimo_id)

    salvar_csv_valido(df_filtrado,OUTPUT_DIR/'registros_validos.csv')

    salvar_csv_invalido(registros_invalidos,OUTPUT_DIR/'registros_invalidos.csv')

    if df_filtrado.empty:
        logger.info('Nao ha registros novos')

        return 

    
    salvar_banco(df_filtrado)

    executar_sql(SQL_DIR/'limpar_tabelas.sql')

    executar_sql(SQL_DIR/'carregar_tabelas.sql')

    novo_ultimo_id=obter_maior_id(df_filtrado)

    registrar_ultimo_id(novo_ultimo_id,'pipeline_incremental')

    logger.info(f'Pipeline executado com sucesso. ultimo_id_processado:{ultimo_id} novo ultimo id : {novo_ultimo_id}')

    