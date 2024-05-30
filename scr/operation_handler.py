import re
from collections import Counter


def find_in_data(data: list, to_find: str) -> list:
    """Принимает список словарей и строку, которую необходимо найти в описании
    и возвращает список словарей, в описании которых есть эта строка"""
    sorted_data = []
    for operation in data:
        if "description" in operation and re.search(to_find, operation["description"]):
            sorted_data.append(operation)
    return sorted_data


def count_by_categories(data: list, categories: list) -> dict:
    """Принимает списки операций и категорий и возвращает словарь
    с названием категории и количеством относящихся к ней операций"""
    counted_dict = Counter(operation["description"] for operation in data if "description" in operation)
    return {category: counted_dict[category] for category in categories}
