import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

def read_json(filename: str) -> list:
    try:
        with open(filename, encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def transaction_sum(transaction: dict) -> float:
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js', headers={"apikey": api_key}, timeout=3)
    data = response.json()
    if transaction['operationAmount']["currency"]['code'] == 'RUB':
        amount = float(transaction['operationAmount']['amount'])
        return amount
    else:
        valute = transaction['operationAmount']["currency"]['code']
        currency = data['Valute'][valute]['Value']
        amount = float(transaction['operationAmount']['amount'])
        return amount * currency

print(transaction_sum({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
    "amount": "8221.37",
    "currency": {
        "name": "USD",
        "code": "USD"
    }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
}))