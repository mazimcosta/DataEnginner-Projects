==========================================================
BOSS FIGHT — ETL V2
PROJETO COMPLETAMENTE NOVO
==========================================================

REGRAS

Esta Boss Fight deve ser desenvolvida do zero.

É proibido copiar:

- extractor.py
- transformer.py
- loader.py
- pipeline.py
- main.py

do projeto anterior.

O conhecimento pode ser reutilizado.

O código deve ser escrito novamente.

==========================================================
CENÁRIO

Uma empresa de logística deseja acompanhar todas
as entregas realizadas diariamente.

Os dados chegam em um CSV bruto contendo erros de
digitação, valores ausentes, formatos diferentes
e inconsistências.

Seu objetivo é construir um pipeline ETL capaz de
transformar esses dados e carregá-los no PostgreSQL.

==========================================================
ARQUITETURA OBRIGATÓRIA

projeto_entregas/

│

├── extractor.py

├── transformer.py

├── loader.py

├── pipeline.py

├── main.py

├── .env

├── entregas.csv

└── README.md

==========================================================
BANCO DE DADOS

Criar um banco chamado:

logistica

Criar uma tabela chamada:

entregas

A modelagem deverá ser feita pelo estudante.

==========================================================
RESPONSABILIDADES

extractor.py

Responsável por:

- ler o CSV
- retornar DataFrame

----------------------------------------------------------

transformer.py

Responsável por:

- tratar valores nulos
- limpar textos
- corrigir inconsistências
- aplicar regras de negócio
- remover registros inválidos
- criar colunas derivadas

----------------------------------------------------------

loader.py

Responsável por:

- conectar ao PostgreSQL
- inserir os registros
- realizar commit
- fechar conexão

----------------------------------------------------------

pipeline.py

Responsável apenas por orquestrar:

Extrair

↓

Transformar

↓

Carregar

----------------------------------------------------------

main.py

Responsável apenas por iniciar o pipeline.

==========================================================
REGRAS DE NEGÓCIO

1.

filial

Obrigatório.

Caso esteja vazio:

preencher com

"Não Informado"

----------------------------------------------------------

2.

motorista

Obrigatório.

Caso esteja vazio:

preencher com

"Motorista Não Informado"

----------------------------------------------------------

3.

status_entrega

Padronizar:

entregue

ENTREGUE

Entregue

↓

Entregue

----------------------------------------------------------

4.

cidade

Padronizar utilizando:

strip()

lower()

title()

----------------------------------------------------------

5.

valor_frete

Aceitar:

R$ 1.250,00

850.50

700

Converter para float.

Caso não seja possível converter:

remover registro.

----------------------------------------------------------

6.

peso_kg

Converter para float.

Caso inválido:

remover registro.

----------------------------------------------------------

7.

Criar uma nova coluna:

valor_por_kg

=

valor_frete

/

peso_kg

----------------------------------------------------------

8.

Remover registros:

peso <= 0

ou

valor_frete <= 0

==========================================================
REGRAS DE ARQUITETURA

Cada responsabilidade deverá possuir sua própria função.

Exemplo:

limpar_cidade()

limpar_valor()

tratar_nulos()

remover_invalidos()

criar_valor_por_kg()

processar_dados()

==========================================================
É PROIBIDO

Misturar responsabilidades.

Colocar regras de negócio no pipeline.py.

Colocar SQL no transformer.py.

Colocar limpeza de dados no loader.py.

Usar notebook.

==========================================================
CRITÉRIOS DE APROVAÇÃO

✓ CSV lido corretamente.

✓ Dados tratados.

✓ Valores monetários convertidos.

✓ Dados inválidos removidos.

✓ Nova coluna criada.

✓ Dados inseridos no PostgreSQL.

✓ Projeto modular.

✓ Separação correta das responsabilidades.

==========================================================
DESAFIO EXTRA

Ao finalizar:

Escrever um README contendo:

- objetivo do projeto;
- arquitetura;
- tecnologias utilizadas;
- regras de negócio;
- principais desafios encontrados;
- aprendizados obtidos.

==========================================================
OBJETIVO DA BOSS FIGHT

Comprovar que o estudante é capaz de construir
um pipeline ETL completo sem reutilizar código
de projetos anteriores.

A avaliação será baseada na arquitetura,
organização do código, aplicação das regras
de negócio, qualidade da implementação e
capacidade de justificar as decisões técnicas.
==========================================================