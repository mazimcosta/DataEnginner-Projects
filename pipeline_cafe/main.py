
from src.pipeline import executar_pipeline
from src.logger import logger

if __name__=='__main__':
    logger.info('Iniciando pipeline')
    try:
        executar_pipeline()
    except Exception as error:
        logger.exception(f'Erro na execucao do pipeline: {error}')
        raise
