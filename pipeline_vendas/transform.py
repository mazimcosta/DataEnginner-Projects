
def processar_dados(dados_brutos):
    vendas_validas=[]
    vendas_invalidas=[]
    validas=0
    invalidas=0
    erros={'produto_vazio':0,'preco_vazio':0,'preco_invalido':0,'preco_negativo_zero':0,'quantidade_vazia':0,'quantidade_invalida':0,'quantidade_negativa_zero':0,
           'categoria_vazia':0}
    relatorio={}

    for venda in dados_brutos:

        produto=venda.get('produto')
        if not produto or not produto.strip():
            invalidas+=1
            vendas_invalidas.append({'venda':venda,'erro':'produto_vazio'})
            erros['produto_vazio']+=1
            continue

        preco=venda.get('preco')
        if not preco or not preco.strip():
            invalidas+=1
            vendas_invalidas.append({'venda':venda,'erro':'preco_vazio'})
            erros['preco_vazio']+=1
            continue

        try:
            preco=round(float(preco),2)
        except (ValueError,TypeError):
            invalidas+=1
            vendas_invalidas.append({'venda':venda,'erro':'preco_invalido'})
            erros['preco_invalido']+=1
            continue

        if preco<=0:
            invalidas+=1
            vendas_invalidas.append({'venda':venda,'erro':'preco_negativo_zero'})
            erros['preco_negativo_zero']+=1
            continue

        quantidade=venda.get('quantidade')
        if not quantidade or not quantidade.strip():
            invalidas+=1
            vendas_invalidas.append({'venda':venda,'erro':'quantidade_vazia'})
            erros['quantidade_vazia']+=1
            continue

        try:
            quantidade=int(quantidade)

        except (ValueError,TypeError):
            invalidas+=1
            vendas_invalidas.append({'venda':venda,'erro':'quantidade_invalida'})
            erros['quantidade_invalida']+=1
            continue

        if quantidade<=0:
            invalidas+=1
            vendas_invalidas.append({'venda':venda,'erro':'quantidade_negativa_zero'})
            erros['quantidade_negativa_zero']+=1
            continue

        categoria=venda.get('categoria')
        if not categoria or not categoria.strip():
            invalidas+=1
            vendas_invalidas.append({'venda':venda,'erro':'categoria_vazia'})
            erros['categoria_vazia']+=1
            continue

        faturamento=round(preco * quantidade,2)
        vendas_validas.append({'produto':produto,'preco':preco,'quantidade':quantidade,'categoria':categoria,'faturamento':faturamento})

    faturamento_total=sum(venda['faturamento'] for venda in vendas_validas)
    faturamento_total= round(faturamento_total,2)
    validas= len(vendas_validas)
    relatorio={'validas':validas,'invalidas':invalidas,'erros':erros,'faturamento_total':faturamento_total}

    return vendas_validas,vendas_invalidas,relatorio



