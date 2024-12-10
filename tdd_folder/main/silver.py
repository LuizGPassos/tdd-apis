import pandas as pd

silver = pd.read_json("./bronze/stocks_data.json")

silver['date'] = pd.to_datetime(silver['date']).dt.date

silver.to_parquet("./silver/stocks_data_silver.parquet")

print(silver)