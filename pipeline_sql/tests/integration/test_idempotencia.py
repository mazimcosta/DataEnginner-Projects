from src.loader import conectar
import psycopg2
from src.pipeline import executar_pipeline

def consultar_tabela(nome_tabela:str):

    conexao=conectar()
    cursor=conexao.cursor()

    cursor.execute(f"""SELECT COUNT(*) FROM {nome_tabela} """)
    dado= cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return dado
    

def test_idempotencia():
    executar_pipeline()
    bronze_1=consultar_tabela('bronze_mercado')
    silver_1=consultar_tabela('silver_mercado')
    gold_1=consultar_tabela('gold_faturamento_categoria')
    
    executar_pipeline()
    bronze_2=consultar_tabela('bronze_mercado')
    silver_2=consultar_tabela('silver_mercado')
    gold_2=consultar_tabela('gold_faturamento_categoria')
    




    assert bronze_1 == bronze_2
    assert silver_1 == silver_2
    assert gold_1 == gold_2
