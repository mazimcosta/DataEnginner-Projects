
from src.pipeline import executar_pipeline
from src.logger import logger

if __name__=='__main__':
    try:
            
        logger.info('Iniciando pipeline')
        executar_pipeline()
        
    except Exception as error:
        logger.error(f'Falha na execucao do pipeline:{error}')
        