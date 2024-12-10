import requests
from dotenv import load_dotenv
import os
import json
import time


load_dotenv()
api_key = os.getenv("API_KEY")

symbols = ['AAPL', 'TSLA', 'UNH', 'MSFT', 'RBLX', 'NVDA', 'INTC', 'F', 'NKE', 'SHEL']


base_url = "https://api.stockdata.org/v1/data/eod"
start_date = '2024-11-22'
end_date = '2024-12-10'

stock_list = []

for symbol in symbols:
    try:

        params = {
            'symbols': symbol,
            'api_token': api_key,
            'date_from': start_date,
            'date_to': end_date,
        }


        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()


        for record in data.get('data', []): 
            record['symbol'] = symbol  


        stock_list.extend(data.get('data', []))

        print(f"Dados obtidos para {symbol}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados para {symbol}: {e}")


with open("./bronze/stocks_data.json", "w") as file:
    json.dump(stock_list, file, indent=4)

print("Coleta de dados concluída.")