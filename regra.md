import psycopg2

def carregar_banco(dados_brutos: list):
    # 1. Transformar a lista de dicionários em uma lista de tuplas
    lista_para_insercao = []
    
    for dado in dados_brutos:
        # Precisamos converter a idade para int, igual fizemos na transformação
        try:
            idade = int(dado.get('age'))
        except (ValueError, TypeError):
            continue # Ignora linhas corrompidas
            
        genero = dado.get('gender')
        plataforma = dado.get('platform_usage')
        
        # Monta a tupla e adiciona na lista da caçamba
        lista_para_insercao.append((idade, genero, plataforma))

    # 2. A Query de Inserção (com %s para proteger contra SQL Injection)
    query_insert = """
        INSERT INTO raw_mental_health (idade, genero, plataforma) 
        VALUES (%s, %s, %s)
    """

    # 3. A Conexão com o Banco de Dados
    try:
        print("Conectando ao banco de dados...")
        conexao = psycopg2.connect(
            dbname="saude_mental", 
            user="postgres", 
            password="SUA_SENHA_AQUI", # Coloque a senha do seu pgAdmin
            host="localhost", 
            port="5432"
        )
        
        cursor = conexao.cursor()
        
        # 4. A MÁGICA: O caminhão despejando a carga de uma vez só!
        print("Injetando os dados em lote...")
        cursor.executemany(query_insert, lista_para_insercao)
        
        # Salva as alterações fisicamente no banco
        conexao.commit()
        print(f"Sucesso! {cursor.rowcount} linhas inseridas na tabela raw_mental_health.")

    except Exception as e:
        # Se der erro, cancela a transação para não sujar o banco
        print(f"Erro na conexão/inserção: {e}")
        if 'conexao' in locals():
            conexao.rollback()
            
    finally:
        # Boas práticas: sempre fechar a porta ao sair
        if 'conexao' in locals():
            cursor.close()
            conexao.close()
            print("Conexão encerrada.")
