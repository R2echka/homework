from datetime import datetime as dt
from typing import Optional

# import sys, os
# sys.path.append(os.getcwd())
# без этих двух строчек код не работает, по крайней мере в VSCode
from scr.masks import bill_mask, card_mask


def mask(info: str) -> Optional[str]:
    """Соединение функций масок в одну"""
    if "Счет" in info:
        mask = bill_mask(info.split()[-1])
        if mask:
            return f"Счет {mask}"
    else:
        card_info = info.split()
        card_number = card_info[-1]
        mask = card_mask(card_number)
        if mask:
            return " ".join(card_info[:-1]) + " " + mask
    return None


def date_correction(date: str) -> str:
    """Форматирует дату"""
    formated_date = dt.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return formated_date.strftime("%d.%m.%Y")
