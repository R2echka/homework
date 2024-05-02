def filter_by_currency(list_: list, currency: str) -> GeneratorExit:
    for i in list_:
        if i['operationAmount']['currency']['code'] == currency.upper():
            yield i
