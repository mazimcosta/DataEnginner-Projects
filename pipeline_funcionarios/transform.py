
def processar_dados(dados_brutos):
    validos=0
    invalidos=0
    funcionarios_validos=[]
    funcionarios_invalidos=[]
    erros={'nome_vazio':0,'email_invalido':0,'salario_vazio':0,'salario_invalido':0,'salario_negativo_ou_zero':0,'departamento_vazio':0}

    for funcionario in dados_brutos:

        nome=funcionario.get('nome')
        if not nome or not nome.strip():
            invalidos+=1
            funcionarios_invalidos.append({'funcionario':funcionario,'erro':'nome_vazio'})
            erros['nome_vazio']+=1
            continue

        email=funcionario.get('email')
        if not email or not email.strip():
            invalidos+=1
            funcionarios_invalidos.append({'funcionario':funcionario,'erro':'email_invalido'})
            erros['email_invalido']+=1
            continue

        if '@' not in email or '.' not in email:
            invalidos+=1
            funcionarios_invalidos.append({'funcionario':funcionario,'erro':'email_invalido'})
            erros['email_invalido']+=1
            continue

        salario=funcionario.get('salario')
        if not salario or not salario.strip():
            invalidos+=1
            funcionarios_invalidos.append({'funcionario':funcionario,'erro':'salario_vazio'})
            erros['salario_vazio']+=1
            continue

        try:
            salario=float(salario)
            salario=round(salario,2)
        except (ValueError,TypeError):
            invalidos+=1
            funcionarios_invalidos.append({'funcionario':funcionario,'erro':'salario_invalido'})
            erros['salario_invalido']+=1
            continue

        if salario<=0:
            invalidos+=1
            funcionarios_invalidos.append({'funcionario':funcionario,'erro':'salario_negativo_ou_zero'})
            erros['salario_negativo_ou_zero']+=1
            continue

        departamento=funcionario.get('departamento')
        if not departamento or not departamento.strip():
            invalidos+=1
            funcionarios_invalidos.append({'funcionario':funcionario,'erro':'departamento_vazio'})
            erros['departamento_vazio']+=1
            continue

        if salario<4000:
            faixa_salarial= 'junior'
        elif salario<=9000:
            faixa_salarial = 'pleno'
        else:
            faixa_salarial = 'senior'
        
        funcionarios_validos.append({'nome':nome,'email':email,'salario':salario,'departamento':departamento,'faixa_salarial':faixa_salarial})
    
    validos=len(funcionarios_validos)
    folha_total = sum(funcionario['salario'] for funcionario in funcionarios_validos)
    folha_total = round(folha_total,2)
    media_salarial= folha_total / len(funcionarios_validos) if len(funcionarios_validos)>0 else 0
    media_salarial = round(media_salarial,2)
    relatorio={'validos':validos,'invalidos':invalidos,'erros':erros,'folha_total':folha_total,'media_salarial':media_salarial}

    return funcionarios_validos,funcionarios_invalidos,relatorio


