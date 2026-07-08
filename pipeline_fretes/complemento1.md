# COMPLEMENTO 1 — SIMULAÇÃO DO DIA A DIA DE UM ENGENHEIRO DE DADOS

## Objetivo

Treinar atividades que fazem parte da rotina de um Engenheiro de Dados e que normalmente não aparecem em cursos:

- investigar pipelines quebrados;
- analisar logs;
- descobrir causa raiz;
- diagnosticar dados inconsistentes;
- otimizar consultas;
- atender solicitações de analistas.

O foco não é escrever código novo.

O foco é aprender a investigar antes de alterar qualquer coisa.

---

# MÓDULO 0 — LEITURA DE LOGS

## Objetivo

Aprender a interpretar logs de erro.

Sem essa habilidade, qualquer incidente em produção vira tentativa e erro.

---

## O que um log possui

Todo log possui três partes.

### 1. Timestamp

Exemplo

```
2025-07-01 03:42:17
```

Serve para descobrir quando ocorreu o problema.

---

### 2. Nível

```
INFO
WARNING
ERROR
CRITICAL
```

---

### 3. Mensagem + Traceback

Exemplo

```
Traceback (most recent call last):

File "loader.py", line 42

cursor.execute(...)

psycopg2.OperationalError:

could not connect to server
```

---

## Como ler um traceback

Sempre leia de baixo para cima.

A última linha normalmente contém o erro verdadeiro.

As linhas superiores mostram apenas o caminho percorrido.

---

## Exercício

Explique:

- onde ocorreu o erro;
- qual foi o erro;
- qual seria sua primeira hipótese;
- qual seria sua primeira investigação.

---

# CENÁRIO 1 — PIPELINE QUEBRADO

## Situação

O pipeline funcionava normalmente.

Hoje ele parou de executar.

Log

```
Traceback (most recent call last):

File "loader.py", line 38

cursor.execute(query)

psycopg2.OperationalError:

connection refused

Is the server running on localhost
and accepting TCP/IP connections?
```

---

## Responda

1.

Qual é o erro real?
### O pipeline nao conseguiu se conectar ao banco de dados pq sua conexao foi rejeitada
---

2.

Onde ele ocorreu?
### no loader ou na funcao carregar_banco
---

3.

Quais hipóteses você levantaria?
### mudança de senha do administrador do banco ou possivel erro de digitação nos campos senha,usuario
---

4.

Quais verificações faria antes de alterar o código?
### Verificaria se as variaveis de ambiente estao corretas como database,user,password.
---

5.

Como confirmaria a causa raiz?
### Se estiverem corretas as variaveis do env e mesmo assim houver erro entraria em contato com o administrador do banco de dados ou a chefia imediata.
---

## Critério de Aprovação

Encontrar a causa sem modificar código.

---

# CENÁRIO 2 — DADO INCONSISTENTE

## Situação

O analista informa:

```
O CSV possui 100 registros.

Mas apenas 87 chegaram ao PostgreSQL.
```

Você possui:

- CSV original;
- DataFrame tratado;
- tabela PostgreSQL.

---

## Responda

Explique passo a passo como investigaria.

Não escreva código.

Descreva sua estratégia.
### Alguma linha foi descartada por erro na execução da funcao processar dados como remover invalidos antes de tratar uma coluna de precos com precos no formato string ou uma regra de negocio acabou excluindo linhas conforme o procedimento.
---

## Critério de Aprovação

Encontrar em qual etapa os registros foram perdidos.

---

# CENÁRIO 3 — QUERY LENTA

## Situação

Uma consulta utilizada diariamente pelo Analytics passou de:

```
3 segundos

↓

45 segundos
```

---

## Responda

1.

Qual seria sua primeira ação?
### Tentaria criar um index para agilizar as consultas ou uma CTE
---

2.

Como descobriria o gargalo?
### Procuraria saber se houve erros de conexao ao banco ou se ha muitas requests ocorrendo e se esta em horario de pico.
---

3.

Quais hipóteses levantaria?
### Conexao lenta,varias requisições, excesso de dados sendo inseridos ou consultados.
---

4.

Quando um índice poderia ajudar?
### Quando uma query esta lenta demais para retornar um resultado e o indice corresponde a uma coluna muito pesquisada.
---

5.

Quando um índice não resolveria o problema?
### Quando geralmente as consultas sao feitas de forma diferente por varios programadores como um usa id outro usa id venda
---

## Critério de Aprovação

Investigar antes de propor qualquer otimização.

---

# CENÁRIO 4 — SOLICITAÇÃO DE ANALISTA

## Mensagem recebida

```
Olá.

Preciso consultar:

- total de fretes por cidade;

- peso médio transportado por cidade.

Gostaria de reutilizar essa consulta
sempre que necessário.
```

---

## Responda

Antes de escrever SQL.

1.

Quais perguntas faria ao analista?
### Se ele deseja um relatorio completo ou apenas saber o valor especifico para uma cidade e se as consultas serao frequentes.
Depois.

2.

Criaria uma View ou apenas um SELECT?

Explique.
### Se as consultas forem frequentes eu criaria uma view para facilitar.
---

3.

Qual seria o nome da View?
### Frete_por_cidade
---

4.

Quais colunas ela retornaria?
### valor total de frete de cada cidade e a media de peso por cidade
---

5.

Escreva um SELECT utilizando essa View.
SELECT cidade,SUM(valor_frete) AS total_frete,AVG(peso_kg) AS media_kg
FROM fretes
GROUP BY cidade
---

## Critério de Aprovação

Pensar primeiro no problema de negócio.

Depois na implementação.

---

# DIÁRIO TÉCNICO

Após cada simulação registrar.

```
Data:

Nome da Simulação:

Sintoma observado:

Hipótese inicial:

O que investiguei:

Causa raiz encontrada:

Correção aplicada:

Erro de raciocínio (se houve):

Tempo até encontrar a causa:
```

---

# RESULTADO ESPERADO

Ao concluir este complemento o estudante deverá ser capaz de:

- interpretar logs;
- ler traceback corretamente;
- levantar hipóteses antes de alterar código;
- investigar pipelines quebrados;
- descobrir causa raiz;
- diagnosticar perda de dados;
- analisar problemas de performance;
- conversar corretamente com analistas;
- propor soluções reutilizáveis;
- registrar investigações em um diário técnico.

O objetivo deste complemento é desenvolver comportamento operacional de Engenharia de Dados, aproximando o treinamento das situações encontradas em produção.