# COMPLEMENTO 2 — COMPORTAMENTO PROFISSIONAL

## Objetivo

Este complemento não ensina novas tecnologias.

Seu objetivo é desenvolver habilidades exigidas no dia a dia de um Engenheiro de Dados:

- trabalhar sob pressão;
- ler código escrito por outras pessoas;
- refatorar código sem alterar comportamento;
- adaptar-se rapidamente a mudanças de regra de negócio.

O foco deixa de ser apenas escrever código e passa a ser manter, evoluir e compreender sistemas existentes.

---

# MÓDULO A — CRONÔMETRO

## Objetivo

Treinar velocidade de execução sem perder qualidade.

## Problema que resolve

No ambiente profissional existe prazo.

É preciso entregar soluções corretas dentro do tempo disponível.

## Execução

O Tech Lead define um tempo máximo para resolver um exercício.

Exemplos:

- limpar um DataFrame;
- corrigir uma função;
- escrever uma consulta SQL;
- encontrar um bug.

Tempo sugerido:

10 minutos.

## Critério de Aprovação

- resolveu dentro do tempo;
- não comprometeu a qualidade;
- explicou o raciocínio utilizado.

---

# MÓDULO B — LEITURA DE CÓDIGO

## Objetivo

Aprender a entender código escrito por outra pessoa.

## Problema que resolve

Na prática profissional você lê muito mais código do que escreve.

## Exercício

### Código

```python
def calcular_valor_por_kg(df):

    df["valor_por_kg"] = (
        df["valor_frete"] / df["peso_kg"]
    ).round(2)

    return df
```

### Explique

1. Qual é a entrada da função?
### um dataframe 

2. O que acontece durante o processamento?
 ### uma nova coluna e criada a partir das colunas valor frente e peso_kg.
3. Qual é a saída?
### retorna o dataframe com a coluna criada
4. Qual problema de negócio essa função resolve?
### Regra de negocio que visa ter a relação custo por kg.
## Regra

Não altere nenhuma linha.

Seu papel é apenas explicar o funcionamento.

## Critério de Aprovação

Explicar corretamente:

- entrada;
- processamento;
- saída;
- objetivo da função.

---

# MÓDULO C — REFATORAÇÃO CONTROLADA

## Objetivo

Melhorar código existente sem alterar comportamento.

## Problema que resolve

Grande parte do código de produção funciona.

O desafio é torná-lo mais legível sem introduzir bugs.

## Exercício

### Código

```python
def limpar(df):

    df=df.dropna(subset=["id_entrega"])

    df["cidade"]=df["cidade"].fillna("Nao informado")

    df["motorista"]=df["motorista"].fillna("Nao informado")

    return df
```
### Resposta
def limpar_invalidos(df):

    df=df.dropna(subset=["id_entrega"])
def tratar_nulos(df):
    df["cidade"]=df["cidade"].fillna("Nao informado")

    df["motorista"]=df["motorista"].fillna("Nao informado")

    return df_tratado

### Refatore pensando em

- organização;
- legibilidade;
- nomenclatura;
- espaçamento;
- boas práticas.

## Regras

Não alterar:

- comportamento;
- resultado;
- regras de negócio.

O DataFrame produzido deve ser exatamente igual ao anterior.

## Critério de Aprovação

Melhorou:

- clareza;
- organização;
- legibilidade.

Sem modificar a lógica.

---

# MÓDULO D — MUDANÇA DE REGRA DE NEGÓCIO

## Objetivo

Treinar adaptação rápida às mudanças do negócio.

## Problema que resolve

Empresas mudam requisitos constantemente.

O profissional precisa saber avaliar impactos antes de alterar código.

---

## Cenário

ANTES

Somente:

- cidade
- motorista

recebiam

```
Nao informado
```

quando estavam vazios.

AGORA

A coluna

```
filial
```

também deverá receber

```
Nao informado
```

quando estiver vazia.

---

## Responda

Sem escrever código.

1.

Em qual função a alteração deve ser feita?
### na função tratar nulos
---

2.

Quais linhas serão impactadas?
### as linhas filial que receberão " nao informado" quando estiverem vazias.
---

3.

Existe risco de quebrar outra regra de negócio?

Explique.
### Sim pois não é possivel gerar metricas por filial mais confiaveis pq algumas filiais estarão como nao informadas.
---

4.

Quais validações manuais devem ser refeitas antes de colocar essa alteração em produção?
### Verificar letras maiusculas,minusculas tipo string e se não ha caracteres especiais nos campos e nem .,\
---

5.

Existe alguma documentação que deveria ser atualizada?
### Documentos de prevenção ou o readme do projeto
Qual?

---

6.

Se outro desenvolvedor fosse revisar sua alteração, quais pontos ele deveria verificar durante o Code Review?
### campos de filial,categoria e cidade que quando nulos devem ser substituidos por nao informado
---

## Critério de Aprovação

Identificar corretamente:

- impacto;
- risco;
- local da alteração;
- validações necessárias;
- documentação afetada.

---

# RESULTADO ESPERADO

Ao concluir este complemento o estudante deverá ser capaz de:

- trabalhar sob pressão;
- compreender código escrito por terceiros;
- refatorar mantendo comportamento;
- analisar impactos antes de alterar regras de negócio;
- justificar decisões técnicas durante um Code Review;
- pensar como um engenheiro responsável pela manutenção de software em produção.

O objetivo deste complemento é desenvolver comportamento profissional, e não apenas habilidade de programação.