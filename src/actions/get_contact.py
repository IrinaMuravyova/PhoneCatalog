from const import FILE_PATH
from prettytable import PrettyTable

def show_all_contacts() -> None:

    table = PrettyTable()
    table.field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]

    with open(FILE_PATH, 'r') as catalog:
        for line in catalog:
            fio = line.strip().split(',')
            table.add_row(['{:<10}'.format(fio[0].split(' ')[0]), 
                           '{:<10}'.format(fio[0].split(' ')[1]), 
                           '{:<10}'.format(fio[0].split(' ')[2]), 
                           line.strip().split(',')[1]])
    
    print(table)

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