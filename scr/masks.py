import sys, os
sys.path.append(os.getcwd())
from scr.logger import log_setup

logger = log_setup()

def card_mask(card_num: str) -> str:
    """Принимаает номер карты и возвращает его маску"""
    if len(card_num) == 16:
        card_num = str(card_num)
        mask = " ".join([card_num[:4], card_num[4:6] + "**", "****", card_num[-4:]])
        logger.info('Применена функция card_mask')
        return mask
    else:
        logger.error('Некорректно введён номер карты')
        return None


def bill_mask(bill_num: str) -> str:
    """Принимает номер счёта и возвращет его маску"""
    if len(bill_num) == 21:
        bill_num = str(bill_num)
        mask = "**" + bill_num[-4:]
        logger.info('Применена функция bill_mask')
        return mask
    else:
        logger.error('Некорректно введён номер счёта')
        return None


