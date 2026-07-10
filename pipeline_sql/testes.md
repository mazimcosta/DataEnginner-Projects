TESTES MÍNIMOS ESSENCIAIS — ETAPA 4 (SQL ANALÍTICO)

OBJETIVO

Garantir que o pipeline funciona corretamente do início ao fim.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TESTE 1 — EXTRACTOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Objetivo:
Garantir que o CSV foi lido corretamente.

O que validar:

✓ DataFrame não está vazio.
✓ Quantidade de registros > 0.

Exemplo:

assert len(df) > 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TESTE 2 — SCHEMA (PYDANTIC)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Objetivo:
Garantir que registros válidos são aceitos
e inválidos são rejeitados.

O que validar:

✓ Registro válido cria VendaSchema.
✓ Registro inválido gera ValidationError.

Exemplo:

pytest.raises(ValidationError)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TESTE 3 — LOADER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Objetivo:
Garantir que apenas os registros válidos
foram carregados para bronze_mercado.

O que validar:

Executar:

SELECT COUNT(*)
FROM bronze_mercado;

Resultado esperado:

Quantidade de linhas da Bronze ==
Quantidade de registros de df_validos.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TESTE 4 — QUERY ANALÍTICA PRINCIPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Objetivo:
Validar a principal transformação da Silver.

Executar:

SELECT
    valor_bruto,
    valor_liquido
FROM silver_mercado
WHERE id_venda = 1;

Comparar com o esperado.

Exemplo usando o CSV:

quantidade = 3
preco_unitario = 4.50
desconto = 0

valor_bruto = 13.50
valor_liquido = 13.50

Fazer assert desses valores.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TESTE 5 — GOLD PRINCIPAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Objetivo:
Garantir que uma tabela Gold foi criada
corretamente.

Executar:

SELECT faturamento_total
FROM gold_faturamento_categoria
WHERE categoria = 'Bebidas';

Comparar com o valor esperado
calculado a partir do CSV.

Não é necessário testar todas as Golds.

Uma Gold é suficiente.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TESTE 6 — LOGGING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Objetivo:
Garantir que o pipeline registra sua execução.

Validar:

✓ início do pipeline.
✓ fim do pipeline.
✓ erro quando ocorre exceção.

Exemplo de mensagens:

logger.info("Iniciando pipeline")

logger.info("Pipeline finalizado com sucesso")

logger.error(...)

Utilizar caplog do pytest.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TESTE 7 — GITHUB ACTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Objetivo:
Garantir execução automática dos testes.

Criar workflow para:

✓ instalar dependências;
✓ executar pytest;
✓ workflow verde a cada push.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CRITÉRIO DE APROVAÇÃO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Extractor aprovado.

✓ Schema aprovado.

✓ Loader aprovado.

✓ Query analítica principal aprovada.

✓ Uma Gold validada.

✓ Logging aprovado.

✓ GitHub Actions executando pytest com sucesso.

Após concluir esses testes, a Etapa 4 poderá ser considerada finalizada e o próximo assunto será:

- Idempotência
- UPSERT
- Full Load x Incremental
- Cursor de processamento
- Recuperação de falhas
- Tabela de controle de execução