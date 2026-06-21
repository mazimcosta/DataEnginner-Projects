

def validar_schema(colunas_arquivo):
    colunas_obrigatorias=['nome','idade','genero']
    
    for coluna in colunas_obrigatorias:
        if coluna not in colunas_arquivo:
            raise ValueError(f'Erro coluna ausente:{coluna}')
        