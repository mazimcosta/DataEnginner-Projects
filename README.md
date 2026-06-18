# 📊 ETL Pipeline: Teen Mental Health Data


## 📝 Sobre o Projeto
Este é um mini-pipeline de dados construído do zero em Python puro. O objetivo principal do projeto foi processar um dataset bruto (`.csv`) sobre o uso de redes sociais e saúde mental de adolescentes, aplicar regras de negócio em lote e exportar um relatório consolidado em formato JSON.

O grande diferencial deste projeto é o foco em **Arquitetura de Software e Performance de Memória**. Em vez de utilizar bibliotecas pesadas de análise de dados (como Pandas) que carregam toda a base na memória RAM, o pipeline processa o arquivo linha a linha (Streaming/I/O) em tempo linear **O(N)**.

## ⚙️ Arquitetura ETL Modular
O código adota o padrão de projeto ETL (Extract, Transform, Load), dividindo as responsabilidades em funções isoladas:

1. **Extract (`extrair_dados`):** Abre a conexão com o arquivo CSV de forma segura utilizando o gerenciador de contexto `with open` e lê os dados brutos utilizando `csv.DictReader`.
2. **Transform (`transformar_dados`):** Aplica a lógica de negócio, limpando os dados, calculando métricas (médias, contagens, valores máximos e mínimos) e ignorando linhas corrompidas sem derrubar o pipeline.
3. **Load (`carregar_dados`):** Persiste o resultado final estruturado em um novo arquivo `.json` no disco local, utilizando tratamento de codificação `UTF-8`.

## 🛡️ Decisões de Engenharia
* **Zero Dependências:** Construído sem bibliotecas externas para demonstrar domínio absoluto de estruturas de dados nativas do Python (Dicionários, Listas, Loops).
* **Programação Defensiva:** Implementação de blocos `try/except` com a instrução `continue` para pular registros sujos ou em branco, garantindo que o sistema não sofra *crash* em produção.
* **Otimização de Algoritmo:** Substituição de funções de ordenamento custosas (`sorted()`) pela lógica nativa de comparação contínua ("pointer approach") para descobrir a plataforma de rede social mais utilizada.

## 📂 Estrutura do Repositório

\`\`\`text
meu_projeto_etl/
│
├── data/
│   ├── raw/                # Onde o CSV original (sujo) deve ser colocado
│   └── processed/          # Onde o relatório final relatorio.json é gerado
│
├── src/
│   └── main.py             # Arquivo orquestrador do pipeline ETL
│
└── README.md
\`\`\`

## 🚀 Como Executar

1. Clone o repositório para a sua máquina local:
   \`\`\`bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   \`\`\`
2. Navegue até a pasta do projeto:
   \`\`\`bash
   cd meu_projeto_etl
   \`\`\`
3. Garanta que o arquivo `Teen_Mental_Health_Dataset.csv` está na pasta `data/raw/`.
4. Execute o orquestrador principal:
   \`\`\`bash
   python src/main.py
   \`\`\`
5. O resultado processado estará disponível em `data/processed/relatorio.json`.

---
*Projeto desenvolvido como parte da trilha de especialização em Engenharia de Dados.*