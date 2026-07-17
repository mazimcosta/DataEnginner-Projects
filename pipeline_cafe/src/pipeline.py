
from config.settings import RAW_DIR,PROCESSED_DIR,SQL_DIR
from src.extractor import extrair_dados
from src.transformer import transformar_dados
from src.logger import logger
from src.schema import validar_schema
from src.sql_executor import executar_sql
from src.loader import (salvar_banco,salvar_csv_invalidos,salvar_csv_valido)
from src.pipeline_control import (buscar_ultimo_id,filtrar_novos_registros,obter_maior_id,atualizar_ultimo_id)

def executar_pipeline():
    df_bruto=extrair_dados(RAW_DIR/'cafe.csv')

    df_limpo=transformar_dados(df_bruto)

    df_valido,registros_invalidos= validar_schema(df_limpo)

    executar_sql(SQL_DIR/'criar_tabelas.sql')

    ultimo_id=buscar_ultimo_id('cafe')

    
    df_filtrado= filtrar_novos_registros(df_valido,ultimo_id)

    if df_filtrado.empty:
        logger.info('Nao ha registros novos')

        salvar_csv_valido(df_valido,PROCESSED_DIR/'registros_validos.csv')

        salvar_csv_invalidos(registros_invalidos,PROCESSED_DIR/'registros_invalidos.csv')

        return
    
    executar_sql(SQL_DIR/'limpar_tabelas.sql')

    salvar_banco(df_filtrado)

    executar_sql(SQL_DIR/'carregar_tabelas.sql')

    novo_ultimo_id=obter_maior_id(df_filtrado)

    atualizar_ultimo_id(novo_ultimo_id,'cafe')

    salvar_csv_valido(df_filtrado,PROCESSED_DIR/'registros_validos.csv')

    salvar_csv_invalidos(registros_invalidos,PROCESSED_DIR/'registros_invalidos.csv')
    logger.info(f'Pipeline finalizado com sucesso. Foram {len(df_filtrado)} registros novos, o ultimo processado foi {ultimo_id} e o recente e {novo_ultimo_id}')    
