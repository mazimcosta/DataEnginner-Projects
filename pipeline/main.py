import logging
import logger
from pipeline import executar_pipeline

if __name__ == '__main__':
        

    logging.info('Iniciando pipeline')

    try:
            
        executar_pipeline()
        logging.info('Pipeline finalizado com sucesso')
    except Exception as error:
        logging.error(f' Pipeline finalizado com erro: {error}')