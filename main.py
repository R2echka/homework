import re

# import sys, os
# sys.path.append(os.getcwd())
import scr.csv_xlsx_reader
import scr.generators
import scr.operation_handler
import scr.processing
import scr.utils
import scr.widget


def main_fail() -> str:
    """Возвращает строку, печатающуюся при неправильном обращении с программой"""
    return "Такой тип операции не поддерживается. Попробуйте ещё раз.\n"


def main() -> None:
    """Основная функция, содержащая все остальные"""
    # Определение файла, с которым пользователь хотел бы работать в формате консольного приложения
    print("Добро пожаловать в программу работы с банковскими транзакциями!")
    file = input(
        """Выберите формат файла:
    1. Json
    2. CSV
    3. Excel\n"""
    )
    if file == "1":
        file_type = "json"
        print("Для обработки выбран json файл.\n")
        data = scr.utils.read_json("data/operations.json")
    elif file == "2":
        file_type = "csv"
        print("Для обработки выбран csv файл.\n")
        data = scr.csv_xlsx_reader.csv_reader("data/transactions.csv")
    elif file == "3":
        file_type = "excel"
        print("Для обработки выбран excel файл.\n")
        data = scr.csv_xlsx_reader.excel_reader("data/transactions_excel.xlsx")
    else:
        print(main_fail())
        main()

    # Сортировка по статусу операции в виде консольного приложения
    print("Выберите статус, по которому необходимо выполнить фильтрацию.")
    status = input("Доступные для сортировки статусы: EXECUTED, CANCELED, PENDING\n")

    if status.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
        print(main_fail())
        main()
    data = scr.processing.sort_by_state(data, status)

    # Сортировка по дате в виде консольного приложения
    to_sort = input("Отсортировать операции по дате? Да/нет \n")
    if to_sort.lower() == "да":
        time = input("По возрастанию или по убыванию?\n")
        if time.lower() == "по возрастанию":
            data = scr.processing.date_sort(data)
        elif time.lower() == "по убыванию":
            data = scr.processing.date_sort(data, "decreasing")
        else:
            print(main_fail())
            main()
    elif to_sort.lower() == "нет":
        pass
    else:
        print(main_fail())
        main()

    # Сортировка по валюте в виде консольного приложения
    to_sort = input("Выводить только рублевые транзакции? Да/нет \n")
    if to_sort.lower() == "да":
        sorted_data = []
        for item in scr.generators.filter_by_currency(data, "RUB", file_type):
            sorted_data.append(item)
        data = sorted_data
    elif to_sort.lower() == "нет":
        pass
    else:
        print(main_fail())
        main()

    # Сортировка по ключевым словам в описании в виде консольного приложения
    to_sort = input("Отфильтровать список операций по определённому слову в описании? Да/нет\n")
    if to_sort.lower() == "да":
        to_find = input("Что вы хотели бы найти? \n")
        data = scr.operation_handler.find_in_data(data, to_find)
    elif to_sort.lower() == "нет":
        pass
    else:
        print(main_fail())
        main()

    print("Распечатываю список транзакций...")
    if data and len(data) != 0:
        print(f"Всего операций в выборке: {len(data)}\n")
        for operation in data:
            print(
                scr.widget.date_correction(operation["date"], file_type),
                next(scr.generators.transaction_descriptions(data)),
            )
            if re.search("Перевод", operation["description"]):
                print(scr.widget.mask(operation["from"]), " -> ", scr.widget.mask(operation["to"]))
            else:
                print(scr.widget.mask(operation["to"]))
            print(f"Сумма: {scr.utils.transaction_sum(operation, file_type)}руб. \n")
    else:
        print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")
    return None


if __name__ == "__main__":
    main()
