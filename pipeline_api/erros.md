ERROS COMETIDOS EM transform.py (API)

1. Tentar usar strip() em um inteiro

Erro:

id = usuario.get("id")

if not id or not id.strip():

Problema:
O campo id da API é inteiro.

Exemplo:

{
    "id": 1
}

Inteiros não possuem o método strip().

Consequência:
AttributeError

Pensamento correto:
Sempre verificar o tipo real do dado antes de aplicar métodos.

--------------------------------------------------

2. Esquecer continue após registrar email inválido

Erro:

if '@' not in email or '.' not in email:
    invalidos += 1
    usuarios_invalidos.append(...)
    erros['email_invalido'] += 1

usuarios_validos.append(...)

Problema:
O usuário era registrado como inválido e válido ao mesmo tempo.

Pensamento correto:
Encontrou erro → registra → continue

--------------------------------------------------

3. Usar id como nome de variável

Erro:

id = usuario.get("id")

Problema:
id já é uma função nativa do Python.

Pensamento correto:

usuario_id = usuario.get("id")

--------------------------------------------------

4. Não seguir exatamente a especificação

Pedido:

id_ausente
nome_ausente
email_ausente

Implementado:

id_vazio
nome_vazio
email_invalido

Problema:
A implementação ficou diferente do requisito.

Pensamento correto:
Implementar exatamente o contrato solicitado.

--------------------------------------------------

5. Repetição excessiva de código

Erro:

usuarios_invalidos.append(...)
erros[...] += 1
invalidos += 1

repetido várias vezes.

Problema:
Código mais difícil de manter.

Pensamento correto:
Quando um padrão começa a se repetir muito,
avaliar extração para uma função auxiliar.

--------------------------------------------------

6. Não pensar primeiro no contrato da função

Antes de programar:
não defini claramente

- entrada
- saída
- estrutura dos válidos
- estrutura dos inválidos

Pensamento correto:
Modelar os dados primeiro.
Codificar depois.

--------------------------------------------------

7. Reaplicar regras do CSV sem verificar a nova origem

Erro:
Copiar validações do pipeline CSV para API.

Exemplo:

if not valor or not valor.strip()

Problema:
A API possui tipos diferentes dos dados do CSV.

Pensamento correto:
Cada fonte de dados deve ser analisada antes de reutilizar validações.