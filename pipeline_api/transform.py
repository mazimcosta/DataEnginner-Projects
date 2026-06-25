
def registrar_erros(usuario:dict,usuarios_invalidos:list,erros:dict,tipo_erro:str):

    usuarios_invalidos.append({
        'usuario_id':usuario.get('id'),
        'nome':usuario.get('name'),
        'email':usuario.get('email'),
        'erro':tipo_erro
    })

    if tipo_erro not in erros:
        erros[tipo_erro]= 1
    else:
        erros[tipo_erro]+=1


def processar_dados(dados:list):
    usuarios_validos=[]
    usuarios_invalidos=[]
    erros={}

    for usuario in dados:

        usuario_id = usuario.get('id')
        if usuario_id is None:
            registrar_erros(usuario,usuarios_invalidos,erros,tipo_erro='id_ausente')
            continue
        
        nome = usuario.get('name')
        if not nome or not nome.strip():
            registrar_erros(usuario,usuarios_invalidos,erros,tipo_erro='nome_ausente')
            continue

        email = usuario.get('email')
        if not email or not email.strip():
            registrar_erros(usuario,usuarios_invalidos,erros,tipo_erro='email_ausente')
            continue

        if '@' not in email or '.' not in email:
            registrar_erros(usuario,usuarios_invalidos,erros,tipo_erro='email_invalido')
            continue

        usuarios_validos.append({'usuario_id':usuario_id,'nome':nome,'email':email})

    validos=len(usuarios_validos)
    invalidos= len(usuarios_invalidos)
    relatorio={'validos':validos,'invalidos':invalidos,'erros':erros}

    return usuarios_validos,usuarios_invalidos,relatorio
            

