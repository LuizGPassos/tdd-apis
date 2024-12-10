import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_parquet("./gold/stocks_data_gold.parquet")

# Converter a coluna 'data' para datetime, caso não seja
df['date'] = pd.to_datetime(df['date'])

# Criar o gráfico
plt.figure(figsize=(10, 6))

# Plotar o preço para cada 'symbol'
for symbol in df['symbol'].unique():
    symbol_data = df[df['symbol'] == symbol]
    plt.plot(symbol_data['date'], symbol_data['preco'], label=symbol)

# Adicionar título e rótulos
plt.title('Preço das Ações ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço')

# Adicionar legenda
plt.legend(title='Symbol')

# Salvar o gráfico em formato PNG
plt.savefig('stocks_prices.png')

