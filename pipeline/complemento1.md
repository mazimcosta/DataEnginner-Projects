COMPLEMENTO 1 — ETAPA 3.2
SIMULAÇÃO DE INCIDENTE REAL

REGRA:
Você é o engenheiro de plantão.
Eu sou o ambiente de produção com problema.
Você deve investigar. Eu não vou entregar a causa.

==================================================
CENÁRIO 1 — PIPELINE QUEBROU
==================================================

SINTOMA:

"O pipeline das 06:00 não carregou os dados no PostgreSQL.
O arquivo de saída CSV foi gerado, mas a tabela vendas não recebeu novos registros.

Aqui está o log:"

2026-07-02 06:00:01 INFO - Iniciando pipeline
2026-07-02 06:00:02 INFO - Iniciando validacao de dados
2026-07-02 06:00:03 INFO - Validacao concluída. Válidos: 148 | Inválidos: 2
2026-07-02 06:00:04 INFO - Iniciando carga no postgres
2026-07-02 06:00:05 ERROR - Erro ao carregar dados para postgres:
relation "vendas" does not exist
LINE 1: INSERT INTO vendas
                    ^
2026-07-02 06:00:05 ERROR - Pipeline finalizado com erro

==================================================
SUA TAREFA
==================================================

Responda sem alterar código ainda:

1. Qual é o erro real?
### Nao foi possivel inserir dados pq a tabela vendas nao foi criada.
2. Em qual camada do pipeline ele aconteceu?
### No loader
3. O problema está na extração, validação, transformação ou carga?
### Na carga
4. Qual é a hipótese de causa raiz?
### Tabela nao criada, poderia ter feito uma query CREATE TABLE IF NOT EXISTS ...
5. Qual seria o primeiro comando SQL ou verificação que você faria?
### SELECT * FROM vendas e verificaria o erro
6. Qual correção você proporia?
### Ao iniciar o loader executar uma query de criação da tabela vendas.
7. Como evitaria esse erro em uma próxima execução?
### Colocaria como observação em um documento chamado prevenção.md

CRITÉRIO DE APROVAÇÃO:
Você precisa chegar na causa raiz apenas lendo o log.

CENÁRIO 2 — CSV GERADO, MAS COM MENOS LINHAS

SINTOMA:

"O pipeline rodou sem quebrar, mas o arquivo output/vendas.csv veio com menos registros do que o esperado."

LOG:

2026-07-02 07:00:01 INFO - Iniciando pipeline
2026-07-02 07:00:02 INFO - Iniciando validacao de dados
2026-07-02 07:00:03 ERROR - Erro de validacao: quantidade Input should be greater than 0
2026-07-02 07:00:03 ERROR - Erro de validacao: preco_unitario Input should be a valid number
2026-07-02 07:00:04 INFO - Validação concluída. Válidos: 92 | Inválidos: 18
2026-07-02 07:00:05 INFO - Carga realizada com sucesso

TAREFA:
1. Qual é o erro real?
### Ha registros invalidos que foram barrados na camada de validacao.
2. O pipeline falhou ou funcionou parcialmente?
### Funcionou mas nao houve tratamento correto dos dados na camada de validação.
3. Onde os registros rejeitados deveriam estar?
### Em um csv separado para auditoria.
4. Qual hipótese investigar primeiro?
### Erro ao inspecionar os dados com explorer.ipynb antes da criação de schema.py
5. O que você reportaria para o time de dados?
### Verificar tipos de dados que podem ser transformados na camada de limpeza.

==================================================

CENÁRIO 3 — ARQUIVO DE ENTRADA NÃO ENCONTRADO

SINTOMA:

"O pipeline não iniciou a extração."

LOG:

2026-07-02 08:00:01 INFO - Iniciando pipeline
2026-07-02 08:00:02 ERROR - Falha na execucao do pipeline: [Errno 2] No such file or directory: 'vendas_sujas.csv'

TAREFA:
1. Qual é o erro real?
### o caminho do arquivo ou o arquivo nao esta no diretorio.
2. Em qual etapa aconteceu?
### extracao
3. Qual arquivo o pipeline esperava?
### vendas_sujas.csv
4. Qual verificação você faria no terminal?
### Verificaria a pasta de origem.
5. Como evitaria esse erro no futuro?
### Estabelecer um padrao de operacao como pasta input e output para todos os projetos.

==================================================

CENÁRIO 4 — ERRO DE CONEXÃO COM POSTGRES

SINTOMA:

"O CSV foi salvo, mas nada foi carregado no banco."

LOG:

2026-07-02 09:00:01 INFO - Iniciando pipeline
2026-07-02 09:00:02 INFO - Validação concluída. Válidos: 150 | Inválidos: 0
2026-07-02 09:00:03 INFO - Iniciando carga no postgres
2026-07-02 09:00:04 ERROR - Erro ao carregar dados para postgres:
could not connect to server: Connection refused
Is the server running on host "localhost" and accepting TCP/IP connections on port 5432?

TAREFA:
1. Qual é o erro real?
### a porta de conexao esta errada ou mal digitada
2. O problema está no código ou na infraestrutura?
### No codigo pq a conexao referente a port nao acontece.
3. Qual comando você usaria para verificar o banco?
### verificaria em qual port o banco esta executando.
4. Qual variável de ambiente pode estar errada?
### port
5. Como evitaria esse erro em produção?
### Colocaria em readme.md ou em documento de observação e prevenção.
==================================================

CENÁRIO 5 — COLUNA ESPERADA NÃO EXISTE

SINTOMA:

"O pipeline quebrou na transformação."

LOG:

2026-07-02 10:00:01 INFO - Iniciando pipeline
2026-07-02 10:00:02 INFO - Validação concluída. Válidos: 150 | Inválidos: 0
2026-07-02 10:00:03 ERROR - Pipeline finalizado com erro: KeyError: 'preco_unitario'

TAREFA:
1. Qual é o erro real?
### Uma mudança nos campos obrigatorios do csv
2. O que significa KeyError?
### Nao foi possivel acessar preco_unitario pq o nome pode ter vindo alterado ou erro no codigo.
3. Qual camada provavelmente falhou?
### Transformer.py
4. Qual hipótese investigar no DataFrame?
### Verificaria se o acesso ao preco_unitario esta sendo feito de maneira correta e se nao contem erros de digitaçao.
5. Como o schema poderia ajudar a evitar esse erro?
### o schema pode verificar os campos ou cabeçalho do csv antes da validaçao para evitar que erros assim cheguem no transformer.

CENÁRIO 6 — REGISTROS INVÁLIDOS NÃO FORAM SALVOS

SINTOMA:

"O pipeline rodou, o CSV final foi gerado, mas o arquivo de inválidos não apareceu."

LOG:

2026-07-02 11:00:01 INFO - Iniciando pipeline
2026-07-02 11:00:02 INFO - Validação concluída. Válidos: 140 | Inválidos: 10
2026-07-02 11:00:03 ERROR - Falha na execucao do pipeline: [Errno 2] No such file or directory: 'output/invalidos.csv'

TAREFA:
1. Qual é o erro real?
### Diretorio ou caminho do arquivo nao foi encontrado.
2. O problema está nos dados ou no caminho do arquivo?
### no caminho do arquivo
3. Qual pasta provavelmente não existe?
### output
4. Qual verificação faria no terminal?
### Verificaria a existencia do arquivo e do diretorio output
5. Como evitaria esse erro no código?
### Colocaria uma observacao em arquivo de prevenção.

==================================================

CENÁRIO 7 — PIPELINE FINALIZA COM SUCESSO, MAS BANCO FICA DUPLICADO

SINTOMA:

"O pipeline rodou três vezes e a tabela vendas ficou com registros duplicados."

LOG:

2026-07-02 12:00:01 INFO - Iniciando pipeline
2026-07-02 12:00:02 INFO - Validação concluída. Válidos: 150 | Inválidos: 0
2026-07-02 12:00:03 INFO - Carga realizada com sucesso

TAREFA:
1. O log mostra erro?
### Nao mas o banco rodou duas vezes a inserção de dados.
2. Qual é o problema real?
### O banco esta salvando dados duplicados.
3. Por que esse tipo de erro não aparece como exception?
### Pq nao é uma falha de execução é uma falha de projeto.
4. Qual coluna poderia ser usada para detectar duplicidade?
### Falha na criação da primary key
5. Que consulta SQL você faria para confirmar?
### SELECT * FROM vendas
6. Como evitaria duplicação em próximas cargas?
### Deixaria um aviso para a criação da tabela com primary key