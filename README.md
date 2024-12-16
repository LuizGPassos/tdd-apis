# Documentação do Projeto: Consumo de API com Arquitetura de Medalhão no Databricks

## Descrição Geral
Este projeto implementa o consumo de uma API de dados financeiros, utilizando a arquitetura de medalhão (Bronze, Silver, Gold). Ele é baseado na extração de dados financeiros de ações por meio de requisições HTTP para a API **StockData.org** e no processamento dos dados em diferentes camadas, até a geração de um dashboard visual.

### Objetivo
Automatizar o consumo, processamento e visualização de dados financeiros, seguindo boas práticas de organização em camadas para análise e tomadas de decisão.

---

## Requisitos
- Python 3.8 ou superior.
- Biblioteca `pandas`.
- Biblioteca `requests`.
- Biblioteca `matplotlib`.
- Biblioteca `dotenv`.
- API Key do **StockData.org**.

---

## Arquivos
O projeto está dividido em quatro scripts principais, correspondentes às camadas da arquitetura de medalhão e a visualização.

### 1. **Bronze Layer** (`bronze.py`)
#### Função:
Realiza a extração dos dados da API e os armazena em formato JSON na camada "Bronze".

#### Principais Funcionalidades:
- Utiliza a API Key armazenada em um arquivo `.env`.
- Faz requisições para a API **StockData.org**.
- Verifica a existência de um arquivo `stocks_data.json` na camada bronze:
  - Caso exista, atualiza os dados a partir da última data registrada.
  - Caso contrário, inicia a coleta de dados do zero.
- Salva os dados coletados em um arquivo JSON em `./bronze/stocks_data.json`.

#### Estrutura da Saída:
- Arquivo: `stocks_data.json`
- Formato: JSON

---

### 2. **Silver Layer** (`silver.py`)
#### Função:
Realiza o processamento inicial dos dados da camada bronze e os transforma em um formato parquet para a camada "Silver".

#### Principais Funcionalidades:
- Converte a coluna `date` para o formato de data.
- Salva os dados no formato Parquet em `./silver/stocks_data_silver.parquet`.

#### Estrutura da Saída:
- Arquivo: `stocks_data_silver.parquet`
- Formato: Parquet

---

### 3. **Gold Layer** (`gold.py`)
#### Função:
Realiza o enriquecimento e agregação dos dados da camada silver para a camada "Gold".

#### Principais Funcionalidades:
- Calcula o preço médio das ações como a média entre `open` e `close`.
- Adiciona uma coluna `codigo_acao` para identificação única.
- Salva os dados no formato Parquet em `./gold/stocks_data_gold.parquet`.

#### Estrutura da Saída:
- Arquivo: `stocks_data_gold.parquet`
- Formato: Parquet

---

### 4. **Dashboard** (`dash.py`)
#### Função:
Gera uma visualização gráfica dos preços das ações ao longo do tempo.

#### Principais Funcionalidades:
- Carrega os dados da camada gold em `./gold/stocks_data_gold.parquet`.
- Plota os preços das ações (`preco`) por símbolo (`symbol`) ao longo das datas.
- Salva o gráfico gerado em um arquivo PNG (`stocks_prices.png`).

#### Saída:
- Arquivo: `stocks_prices.png`
- Formato: Imagem PNG
