import pandas as pd
import pytest
from src.extractor import extrair_dados
from config.settings import RAW_DIR

def test_arquivo_valido():

    df=extrair_dados(RAW_DIR/'cafe.csv')

    assert df is not None
    assert isinstance(df,pd.DataFrame)
