

def registrar_erros(produto:dict,produtos_invalidos:list,erros:dict,tipo_erro:str):

    produtos_invalidos.append({
        'produto_id':produto.get('id'),
        'nome':produto.get('title'),
        'preco':produto.get('price'),
        'descricao':produto.get('description'),
        'erro':tipo_erro

    })
    if tipo_erro not in erros:
        erros[tipo_erro]= 1
    else:
        erros[tipo_erro]+=1


def processar_dados_API(dados:list):
    produtos_validos=[]
    produtos_invalidos=[]
    erros={}
    relatorio={}

    for produto in dados:

        produto_id = produto.get('id')
        if produto_id is None:
            registrar_erros(produto,produtos_invalidos,erros,tipo_erro='id_ausente')
            continue

        nome = produto.get('title')
        if not nome or not nome.strip():
            registrar_erros(produto,produtos_invalidos,erros,tipo_erro='nome_ausente')
            continue

        preco = produto.get('price')
        if preco is None:
            registrar_erros(produto,produtos_invalidos,erros,tipo_erro='preco_ausente')
            continue

        try:
            preco= float(preco)
        except (ValueError,TypeError):
            registrar_erros(produto,produtos_invalidos,erros,tipo_erro='preco_invalido')
            continue

        if preco<=0:
            registrar_erros(produto,produtos_invalidos,erros,tipo_erro='preco_negativo_ou_zero')
            continue

        descricao = produto.get('description')
        if not descricao or not descricao.strip():
            registrar_erros(produto,produtos_invalidos,erros,tipo_erro='descricao_ausente')
            continue

        categoria = None
        rating = None
        classificacao = None

        categoria = produto.get('category')
        rating = produto.get('rating')
        if rating:
            classificacao = rating.get('rate')

        produtos_validos.append({'produto_id':produto_id,'nome':nome,'preco':preco,'descricao':descricao,'categoria':categoria,'classificacao':classificacao})
    
    preco_medio = sum(produto['preco'] for produto in produtos_validos)/ len(produtos_validos) if len(produtos_validos) >0 else 0
    validos= len(produtos_validos)
    invalidos = len(produtos_invalidos)
    relatorio = {'validos':validos,'invalidos':invalidos,'erros':erros,'preco_medio':preco_medio}

    return produtos_validos,produtos_invalidos,relatorio



