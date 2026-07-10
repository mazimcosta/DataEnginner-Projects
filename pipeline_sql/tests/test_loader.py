import pandas as pd
from src.extractor import extrair_dados
import  psycopg2
from src.schema import validar_schema
from config.settings import INPUT_DIR
from src.loader import conectar

def test_validar_registros_banco():
    conexao=conectar()
    cursor=conexao.cursor()

    try:
        df_bruto=extrair_dados(INPUT_DIR/'mercado.csv')
        df_valido,*_=validar_schema(df_bruto)

        cursor.execute("""SELECT COUNT(*) FROM bronze_mercado """)
        bronze_mercado=cursor.fetchone()[0]

        assert len(df_valido) == bronze_mercado
    
    finally:
        cursor.close()
        conexao.close()
    
