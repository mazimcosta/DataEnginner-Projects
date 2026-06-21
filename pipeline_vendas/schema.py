
def validar_schema(colunas_arquivo):
    colunas_obrigatorias=['produto','preco','quantidade','categoria']
    for coluna in colunas_obrigatorias:
        if coluna not in colunas_arquivo:
            raise ValueError(f'erro coluna ausente: {coluna}')
        
