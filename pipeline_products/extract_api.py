
import requests

def extrair_dados_API(url:str):

    try:
        response= requests.get(url,timeout=5)

        if response.status_code != 200:
            raise ValueError('Falha na API status code:{response.status_code=}')
        return response.json()
    
    except requests.exceptions.ConnectionError:
        raise ValueError('Erro de conexão com a API')
    
    except requests.exceptions.Timeout:
        raise ValueError('Erro tempo limite excedido')
    
