
import pytest
from config.settings import LOG_FILE

def test_logs():

    with open(LOG_FILE,'r',encoding='utf-8') as arquivo:
        logs=arquivo.read()

    assert 'Iniciando pipeline' in logs
    assert 'Pipeline finalizado com sucesso' in logs

    