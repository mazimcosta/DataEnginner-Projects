
import requests

def extrair_dados_api(url:str):
    
    try:
            
        response=requests.get(url,timeout=5)
        if response.status_code != 200:
            raise ValueError(f'Erro falha  na  API: {response.status_code}')
        
        
        return response.json()
    
    except requests.exceptions.ConnectionError:
        raise ValueError('Erro falha de conexao com  a API')
    
    except requests.exceptions.Timeout:
        raise ValueError('Tempo limite de conexao excedido')

