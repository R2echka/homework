import re
import sys, os
sys.path.append(os.getcwd())
import scr
from scr import csv_xlsx_reader, decorators, generators, operation_handler, processing, utils, widget

import scr.utils
import scr.widget

def main_fail() -> str:
    return 'Такой тип операции не поддерживается. Попробуйте ещё раз.\n'


def main():
    def file_format():
        print('Добро пожаловать в программу работы с банковскими транзакциями!')
        file = input('''Выберите формат файла: 
    1. Json
    2. CSV
    3. Excel\n''')
        
        if file == '1':
            print('Для обработки выбран json файл.\n')
            return scr.utils.read_json('data/operations.json'), 'json'
        elif file == '2':
            print('Для обработки выбран csv файл.\n')
            return scr.csv_xlsx_reader.csv_reader('data/transactions.csv'), 'csv'
        elif file == '3':
            print('Для обработки выбран excel файл.\n')
            return scr.csv_xlsx_reader.excel_reader('data/transactions_excel.xlsx'), 'excel'
        else:
            print(main_fail())
            file_format()
            return [], ''
    data, file_type = file_format()
    def status_sort():
        print('Выберите статус, по которому необходимо выполнить фильтрацию.')
        status = input('Доступные для сортировки статусы: EXECUTED, CANCELED, PENDING\n')

        if status.upper() not in ('EXECUTED', 'CANCELED', 'PENDING'):
            print(main_fail())
            status_sort()
        return scr.processing.sort_by_state(data, status)
    data = status_sort()
    def date_sort():
        to_sort = input('Отсортировать операции по дате? Да/нет \n')
        if to_sort.lower() == 'да':
            time = input('По возрастанию или по убыванию?\n')
            if time.lower() == 'по возрастанию':
                return scr.processing.date_sort(data)
            elif time.lower() == 'по убыванию':
                return scr.processing.date_sort(data, 'decreasing')
            else:
                print(main_fail())
                date_sort()
                return []
        elif to_sort.lower() == 'нет':
            return data
        else:
            print(main_fail())
            date_sort()
            return []
    data = date_sort()
    
    def only_rub():
        to_sort = input('Выводить только рублевые транзакции? Да/нет \n')
        if to_sort.lower() == 'да':
            sorted_data = []
            for item in scr.generators.filter_by_currency(data, 'RUB', file_type):
                sorted_data.append(item)
            return sorted_data
        elif to_sort.lower() == 'нет':
            return data
        else:
            print(main_fail())
            only_rub()
            return []
    data = only_rub()

    def word_sort():
        to_sort = input('Отфильтровать список операций по определённому слову в описании? Да/нет \n')
        if to_sort.lower() == 'да':
            to_find = input('Что вы хотели бы найти? \n')
            return scr.operation_handler.find_in_data(data, to_find)
        elif to_sort.lower() == 'нет':
            return data
        else:
            print(main_fail())
            word_sort()
            return []
    data = word_sort()

    print('Распечатываю список транзакций...')
    if data and len(data) != 0:
        print(f'Всего операций в выборке: {len(data)}\n')
        for operation in data:
            print(f'{scr.widget.date_correction(operation['date'], file_type)} {next(scr.generators.transaction_descriptions(data))}')
            if re.search('Перевод', operation['description']):
                print(f'{scr.widget.mask(operation['from'])} -> {scr.widget.mask(operation['to'])}')
            else:
                print(scr.widget.mask(operation['to']))
            print(f'Сумма: {scr.utils.transaction_sum(operation, file_type)}руб. \n')
    else:
        print('Не найдено ни одной транзакции подходящей под ваши условия фильтрации')


if __name__ == '__main__':
    main()