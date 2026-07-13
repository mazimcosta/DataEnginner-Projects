from src.extractor import extrair_dados
import pytest
from config.settings import INPUT_DIR

def test_extracao_valida():

    df=extrair_dados(INPUT_DIR/'farmacia_1.csv')

    assert df is not None
    assert len(df) == 10


def test_caminho_arquivo_invalido():

    with pytest.raises(FileNotFoundError):
        df=extrair_dados('vendas.csv')

