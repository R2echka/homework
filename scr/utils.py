import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def read_json(filename: str) -> list:
    """Читает json-файл по переданному пути"""
    try:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def transaction_sum(transaction: dict) -> float:
    """Принимает транзакцию и возвращает её сумму в рублях"""
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js", headers={"apikey": api_key}, timeout=3)
    data = response.json()
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount = float(transaction["operationAmount"]["amount"])
        return float(amount)
    else:
        valute = transaction["operationAmount"]["currency"]["code"]
        currency = data["Valute"][valute]["Value"]
        amount = float(transaction["operationAmount"]["amount"])
        return float(amount * currency)
