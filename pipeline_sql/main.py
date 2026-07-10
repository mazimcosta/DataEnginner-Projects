from src.logger import logger
from src.pipeline import executar_pipeline

if __name__=='__main__':
    logger.info('Iniciando pipeline')

    try:
        executar_pipeline()
        logger.info('Pipeline executado com sucesso')
    except Exception as error:
        logger.error(f'Erro na execucao do pipeline:{error}')

        