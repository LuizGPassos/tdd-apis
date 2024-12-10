import pandas as pd

gold = pd.read_parquet("./silver/stocks_data_silver.parquet")

gold['codigo_acao'] = gold.index
gold['preco'] = (gold['open'] + gold['close']) / 2

gold.to_parquet("./gold/stocks_data_gold.parquet")
print(gold)