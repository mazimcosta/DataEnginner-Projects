import pandas as pd
from src.extractor import extrair_dados
from config.settings import INPUT_DIR
import pytest

def test_caminho_arquivo_valido():
    df=extrair_dados(INPUT_DIR/'mercado.csv')
    
    assert df is not None
    assert len(df)>0


def test_caminho_arquivo_invalido():
    
    with pytest.raises(FileNotFoundError):
        df=extrair_dados(INPUT_DIR/'exemplo.csv')

