def card_mask(card_num: str) -> str:
    """Принимаает номер карты и возвращает его маску"""
    card_num = str(card_num)
    mask = " ".join([card_num[:4], card_num[4:6] + "**", "****", card_num[-4:]])
    return mask


def bill_mask(bill_num: str) -> str:
    """Принимает номер счёта и возвращет его маску"""
    bill_num = str(bill_num)
    mask = "**" + bill_num[-4:]
    return mask
