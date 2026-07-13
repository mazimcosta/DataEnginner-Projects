# TESTES — ETAPA 4 (PARTE 1)

## OBJETIVO

Garantir que Bronze e Silver funcionam corretamente utilizando carga incremental com UPSERT.

==================================================
TESTES UNITÁRIOS
==================================================

## 1. SCHEMA — REGISTRO VÁLIDO

Objetivo

Garantir que um registro válido seja aceito.

Validar:

- criação do schema;
- tipos corretos;
- campos obrigatórios.

--------------------------------------------------

## 2. SCHEMA — REGISTRO INVÁLIDO

Objetivo

Garantir que registros inválidos sejam rejeitados.

Casos mínimos:

- quantidade inválida;
- preco_unitario inválido;
- campo obrigatório ausente.

Validar:

- ValidationError.

--------------------------------------------------

## 3. LOGGING

Objetivo

Garantir que o pipeline registre:

- início;
- sucesso;
- erro.

==================================================
TESTES DE INTEGRAÇÃO
==================================================

## 4. UPSERT NA BRONZE

Objetivo

Validar:

- venda nova é inserida;
- venda existente é atualizada;
- não ocorre duplicidade.

--------------------------------------------------

## 5. UPSERT NA SILVER

Objetivo

Validar:

- venda válida nova é inserida;
- venda válida existente é atualizada;
- valor_bruto e valor_liquido são recalculados.

--------------------------------------------------

## 6. REMOÇÃO DA SILVER

Objetivo

Validar que uma venda que deixou de ser válida
(status cancelado ou quantidade inválida)
é removida da Silver.

A venda deverá permanecer na Bronze.

--------------------------------------------------

## 7. IDEMPOTÊNCIA

Objetivo

Executar a mesma carga duas vezes.

Validar:

- Bronze sem duplicidade;
- Silver sem duplicidade;
- estado final permanece igual.

==================================================
CRITÉRIO DE APROVAÇÃO
==================================================

Todos os testes deverão passar.

A carga incremental não poderá gerar duplicidade.

A Bronze deverá refletir todas as alterações.

A Silver deverá refletir apenas os registros válidos.

O pipeline deverá permanecer idempotente.