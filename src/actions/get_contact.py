from const import FILE_PATH
from prettytable import PrettyTable

def show_all_contacts() -> None:

    table = PrettyTable()
    table.field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]

    with open(FILE_PATH, 'r') as catalog:
        for line in catalog:
            fio = line.strip().split(',')
            # print(fio[0].split(' ')[0])
            table.add_row(['{:<10}'.format(fio[0].split(' ')[0]), '{:<10}'.format(fio[0].split(' ')[1]), '{:<10}'.format(fio[0].split(' ')[2]), line.strip().split(',')[1]])
    
    print(table)

    # table = PrettyTable()
    # table.field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
    # table.add_rows(
    #         [
    #     ["Adelaide", 1295, 1158259, 600.5],
    #     ["Brisbane", 5905, 1857594, 1146.4],
    #     ["Darwin", 112, 120900, 1714.7],
    #     ["Hobart", 1357, 205556, 619.5],
    #     ["Sydney", 2058, 4336374, 1214.8],
    #     ["Melbourne", 1566, 3806092, 646.9],
    #     ["Perth", 5386, 1554769, 869.4],
    # ]
    # )
    # print(table)

def search_name() -> None:
    temp_lst = []
    with open(FILE_PATH, 'r') as catalog:
        for line in catalog:
            temp_lst.append(line)
    print(temp_lst)
    searching_name = input('Введите имя для поиска: ')
    for line in temp_lst:
        if searching_name in line:
            print(line)
        else: print("Контакт с этим именем не найден. ")