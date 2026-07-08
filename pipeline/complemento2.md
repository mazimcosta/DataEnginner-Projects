COMPLEMENTO 2 — ETAPA 3.2
LOGGING + VALIDAÇÃO COM PYDANTIC

OBJETIVO GERAL:
Treinar comportamento profissional em cima do pipeline já construído, sem aprender tecnologia nova.

TEMPO TOTAL:
25 a 35 minutos.

REGRAS:
- Não adicionar biblioteca nova.
- Não mudar arquitetura do projeto.
- Não reescrever o pipeline do zero.
- Trabalhar apenas com: extractor, transformer, loader, pipeline, schema, logger e main.
- Usar logging em vez de print.
- Manter separação entre registros válidos e inválidos.

==================================================
MÓDULO A — CRONÔMETRO
==================================================

TEMPO: 10 minutos.

TAREFA:
Altere o pipeline para salvar os registros inválidos em:

output/invalidos.csv

Hoje eles ainda estão sendo salvos como:

invalidos.csv

CRITÉRIO DE APROVAÇÃO:
- O arquivo output/invalidos.csv é criado.
- O pipeline continua gerando output/vendas.csv.
- Nenhum arquivo inválido fica solto na raiz do projeto.
- O log registra que os inválidos foram salvos.

==================================================
MÓDULO B — LEITURA DE CÓDIGO
==================================================

TEMPO: 5 minutos.

Leia este código e explique sem alterar:

def validar_schema(df):
    logging.info("Iniciando validacao de dados")
    registros_validos = []
    registros_invalidos = []

    for registro in df.to_dict("records"):
        try:
            venda = VendaSchema(**registro)
            registros_validos.append(venda.model_dump())
        except ValidationError as error:
            registros_invalidos.append(registro)
            logging.error(f"Erro de validacao: {error}")

    df_limpo = pd.DataFrame(registros_validos)
    logging.info("Validacao executada com sucesso")

    return df_limpo, registros_invalidos

RESPONDER:
1. Qual é a entrada da função?
2. O que acontece dentro do for?
3. O que o VendaSchema(**registro) faz?
4. Por que usamos model_dump()?
5. O que acontece quando ocorre ValidationError?
6. Qual é a saída da função?
7. Qual responsabilidade essa função tem no pipeline?

CRITÉRIO DE APROVAÇÃO:
Você consegue explicar entrada, processamento, saída e objetivo sem executar o código.

==================================================
MÓDULO C — REFATORAÇÃO CONTROLADA
==================================================

TEMPO: 10 minutos.

TAREFA:
Refatore este trecho do loader.py:

if 'cursor' in locals():
    cursor.close()

if 'conexao' in locals():
    conexao.close()

Para um padrão mais explícito usando:

conexao = None
cursor = None

REGRAS:
- Não alterar o comportamento.
- Não remover rollback.
- Não remover logging.
- Não voltar a usar except Exception.

CRITÉRIO DE APROVAÇÃO:
- conexao e cursor começam como None.
- rollback só acontece se conexao existir.
- cursor.close() só acontece se cursor existir.
- conexao.close() só acontece se conexao existir.
- O código continua capturando psycopg2.Error.

==================================================
MÓDULO D — MUDANÇA DE REGRA DE NEGÓCIO
==================================================

TEMPO: 10 minutos.

NOVA REGRA:
O time de dados pediu que o log da validação informe também a quantidade de registros válidos e inválidos.

Hoje o log final está genérico:

"Validacao executada com sucesso"
### Resposta
def validar_schema(df:pd.DataFrame):
    logging.info('Iniciando validacao de dados')
    registros_validos=[]
    registros_invalidos=[]

    for registro in df.to_dict('records'):

        try:
            venda=VendaSchema(**registro)
            registros_validos.append(venda.model_dump())
        except ValidationError as error:
            registros_invalidos.append(registro)
            logging.error(f'Erro de validacao{error}')

    df_limpo =pd.DataFrame(registros_validos)
    logging.info(f' Validacao executada com sucesso. Sao `{len(registros_validos)} validos e {len(registros_invalidos)} invalidos.')

    return df_limpo,registros_invalidos
Altere para registrar algo como:

"Validação concluída. Válidos: X | Inválidos: Y"

REGRAS:
- Não mudar o retorno da função.
- Não alterar o schema.
- Não alterar o transformer.
- Apenas melhorar o log.

CRITÉRIO DE APROVAÇÃO:
O log final mostra:
- quantidade de registros válidos;
- quantidade de registros inválidos.

==================================================
MÓDULO E — CODE REVIEW
==================================================

TEMPO: 10 minutos.

Revise o código abaixo como se fosse de outro dev:

def salvar_banco(df):
    try:
        conexao = psycopg2.connect(...)
        cursor = conexao.cursor()

        for linha in df.itertuples():
            cursor.execute("INSERT INTO vendas VALUES (...)")

        conexao.commit()

    except Exception as error:
        print(error)

    finally:
        cursor.close()
        conexao.close()

RESPONDER:
1. Quais erros existem?
### Exception generico sem uso de psycopg2.error e uso de print ao inves de loggin.error
2. Por que except Exception é ruim aqui?
### Pq nao e possivel identificar o erro especifico.
3. Por que print(error) é inferior a logging.error?
### pq com logging temos registrado o exato momento em que o pipeline falha e em qual camada.
4. O que acontece se a conexão falhar antes do cursor ser criado?
### o cursor nao existe como objeto.
5. Como deveria ser o padrão correto?
### Criar conexao = None e cursor = None antes de try
CRITÉRIO DE APROVAÇÃO:
Você identifica:
- except Exception genérico;
- uso indevido de print;
- risco de cursor não existir;
- necessidade de rollback;
- necessidade de fechar conexão com segurança;
- uso de psycopg2.Error.

==================================================
ENTREGA FINAL DO COMPLEMENTO 2
==================================================

Ao terminar, responder:

1. O que foi alterado no código?
2. O que ficou mais robusto?
3. Qual erro você evitaria em produção com essas mudanças?
4. Qual parte ainda parece frágil?
5. Qual commit você faria?

SUGESTÃO DE COMMIT:

git add .
git commit -m "refactor: improve logging and database error handling"