from config.settings import LOG_FILE

def test_logging():

    with open(LOG_FILE,'r',encoding='utf-8') as arquivo:

        logs=arquivo.read()

    assert "Iniciando pipeline" in logs
    assert "Pipeline executado com sucesso" in logs