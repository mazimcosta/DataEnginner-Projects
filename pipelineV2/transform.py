


def processar_dados(dados_brutos):
    clientes_validos=[]
    validos=0
    invalidos=0
    clientes_invalidos=[]
    erros={'nome_vazio':0,'idade_vazia':0,'idade_invalida':0,'idade_negativa':0,'genero_vazio':0,'genero_invalido':0}
    relatorio={}

    for dado in dados_brutos:

        nome=dado.get('nome')
        if not nome or not nome.strip():
            invalidos+=1
            erros['nome_vazio']+=1
            clientes_invalidos.append({'dado':dado,'erro':'nome_vazio'})
            continue
        
       
        idade=dado.get('idade')
        if not idade:
            invalidos+=1
            erros['idade_vazia']+=1
            clientes_invalidos.append({'dado':dado,'erro':'idade_vazia'})
            continue
        
        try:
            idade=int(idade)
        except ValueError:
            invalidos+=1
            erros['idade_invalida']+=1
            clientes_invalidos.append({'dado':dado,'erro':'idade_invalida'})
            continue

        
        if idade<0:
            invalidos+=1
            erros['idade_negativa']+=1
            clientes_invalidos.append({'dado':dado,'erro':'idade_negativa'})
            continue


        genero=dado.get('genero')
        if not genero or not genero.strip():
            invalidos+=1
            erros['genero_vazio']+=1
            clientes_invalidos.append({'dado':dado,'erro':'genero_vazio'})
            continue
        

        if genero.lower() not in ['male','female']:
            invalidos+=1
            erros['genero_invalido']+=1
            clientes_invalidos.append({'dado':dado,'erro':'genero_invalido'})
            continue

        clientes_validos.append({'nome':nome,'idade':idade,'genero':genero})

    validos=len(dados_brutos) - invalidos
    relatorio={'validos':validos,'invalidos':invalidos,'erros':erros}
    return clientes_validos,clientes_invalidos,relatorio

