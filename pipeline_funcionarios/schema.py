

def validar_schema(colunas_arquivo):
    if not colunas_arquivo:
        raise ValueError(f'Erro: arquivo sem cabecalho')
    colunas_obrigatorias=['nome','email','salario','departamento']
    for coluna in colunas_obrigatorias:
        if coluna not in colunas_arquivo:
            raise ValueError(f'Erro: coluna obrigatoria ausente {coluna}')