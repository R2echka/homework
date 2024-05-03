def filter_by_currency(list_: list, currency: str) -> GeneratorExit:
    for i in list_:
        if i['operationAmount']['currency']['code'] == currency.upper():
            yield i

def transaction_descriptions(list_:list) -> GeneratorExit:
    for i in list_:
        yield i['description']

def card_number_generator(first: int, last: int) -> GeneratorExit:
    for i in range(first, last+1):
        card_num = f'{i:0>16}'
        yield card_num[:4] + ' ' + card_num[4:8] + ' ' + card_num[8:12] + ' ' + card_num[12:]

for card_number in card_number_generator(1, 10000):
    print(card_number)
