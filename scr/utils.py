import json
import os

import requests
from dotenv import load_dotenv

# import sys, os
# sys.path.append(os.getcwd())
from scr.logger import log_setup

load_dotenv()
api_key = os.getenv("API_KEY")
logger = log_setup()


def read_json(filename: str) -> list:
    """Читает json-файл по переданному пути"""
    try:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Прменена функция read_json")
                return data
            else:
                logger.error("В файле находится не список")
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Что-то координально пошло не так")
        return []


def transaction_sum(transaction: dict, file_type: str) -> float:
    """Принимает транзакцию и возвращает её сумму в рублях"""
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js", headers={"apikey": api_key}, timeout=3)
    data = response.json()
    if file_type == 'json':
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            amount = float(transaction["operationAmount"]["amount"])
            currency = 1.0
        else:
            valute = transaction["operationAmount"]["currency"]["code"]
            currency = data["Valute"][valute]["Value"]
            amount = float(transaction["operationAmount"]["amount"])
    else:
        if transaction["currency_code"] == "RUB":
            amount = float(transaction["amount"])
            currency = 1.0
        else:
            valute = transaction["currency_code"]
            if data['Valute'][valute]:
                currency = data["Valute"][valute]["Value"]
            else:
                currency = 'USD'
            amount = float(transaction["amount"])
    logger.info("Применена функция transaction_sum")
    return float(amount * currency)
