import json


def read_json(filename: str) -> list:
    try:
        with open(filename, encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []