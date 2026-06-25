
def remover_duplicados(produtos_validos):

    ids_vistos = {}
    nova_lista=[]

    for produto in produtos_validos:

        produto_id = produto['produto_id']

        if produto_id not in ids_vistos:
            ids_vistos[produto_id] = True
            nova_lista.append(produto)
        else:
            continue

    return nova_lista