
from src.loader import conectar
import psycopg2
from decimal import Decimal

def test_query_analitica():
    conexao=conectar()
    cursor=conexao.cursor()

    try:
        cursor.execute("""SELECT valor_bruto,valor_liquido FROM silver_mercado WHERE id_venda = 1 """)
        silver_mercado=cursor.fetchone()

        assert silver_mercado[0]==13.50
        assert silver_mercado[1]==13.50

    finally:
        cursor.close()
        conexao.close()

def test_gold_analitica():
    conexao=conectar()
    cursor=conexao.cursor()

    try:
        cursor.execute("""SELECT faturamento_total FROM gold_faturamento_categoria WHERE categoria = 'Bebidas' """)
        faturamento=cursor.fetchone()[0]

        assert faturamento == Decimal('49.80')
        assert faturamento is not None
    finally:
        cursor.close()
        conexao.close()