import requests
from dotenv import load_dotenv
import os
import json
import pandas as pd
from datetime import datetime, timedelta


load_dotenv()
api_key = os.getenv("API_KEY")

symbols = ['AAPL', 'TSLA', 'UNH', 'MSFT', 'RBLX', 'NVDA', 'INTC', 'F', 'NKE', 'SHEL']

base_url = "https://api.stockdata.org/v1/data/eod"

start_date = '2024-11-22'
end_date = '2024-12-10'

stock_list = []

try:
    with open('./bronze/stocks_data.json') as f:
        print(f"Arquivo já existe!")


        bronze_df = pd.read_json('./bronze/stocks_data.json')

        bronze_df['date'] = pd.to_datetime(bronze_df['date'])
        max_date = bronze_df['date'].max()
        print(f"Última data registrada no arquivo: {max_date}")

        start_date = max_date + timedelta(days=1)  
        end_date = start_date + timedelta(days=12)

        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')

        print(f"Novo intervalo de datas: {start_date} a {end_date}")

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

        if stock_list:
            new_data_df = pd.DataFrame(stock_list)

            updated_df = pd.concat([bronze_df, new_data_df], ignore_index=True)

            updated_df = updated_df.drop_duplicates(subset=['date', 'symbol'], keep='last')

            updated_df.to_json('./bronze/stocks_data.json', orient='records', date_format='iso', indent=4)
            print("Arquivo atualizado com novos dados.")

except FileNotFoundError:
    print("Arquivo não encontrado. Iniciando coleta de dados do zero.")

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