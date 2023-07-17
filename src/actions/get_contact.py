from const import FILE_PATH
from prettytable import PrettyTable

def show_all_contacts() -> None:

    table = PrettyTable()
    table.field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]

    with open(FILE_PATH, 'r') as catalog:
        for line in catalog:
            fio = line.strip().split(',')[0]
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
    
    searching_name = input('Введите имя для поиска: ')
    print('\n')

    founded = False 
    for line in temp_lst:
        if searching_name.lower() in line.lower() and searching_name.lower() == (line.strip().split(',')[0].split(' ')[1]).lower():
            print(line)
            founded = True
    if founded == False:
        print("Контакт с этим именем не найден. ")


def search_surname() -> None:

    temp_lst = []

    with open(FILE_PATH, 'r') as catalog:
        for line in catalog:
            temp_lst.append(line)
    
    searching_surname = input('Введите фамилию для поиска: ')
    print('\n')

    founded = False
    for line in temp_lst:
        if searching_surname.lower() in line.lower() and searching_surname.lower() == (line.strip().split(',')[0].split(' ')[0]).lower():
            print(line)
            founded = True
    if founded == False:
        print("Контакт с этой фамилией не найден. ")


def search_middlename() -> None:

    temp_lst = []

    with open(FILE_PATH, 'r') as catalog:
        for line in catalog:
            temp_lst.append(line)
    
    searching_middlename = input('Введите отчество для поиска: ')
    print('\n')

    founded = False
    for line in temp_lst:
        if searching_middlename.lower() in line.lower() and searching_middlename.lower() == (line.strip().split(',')[0].split(' ')[2]).lower():
            print(line)
            founded = True
    if founded == False:
        print("Контакт с этим отчеством не найден. ")


def search_phone_number() -> None:
    temp_lst = []

    with open(FILE_PATH, 'r') as catalog:
        for line in catalog:
            temp_lst.append(line)
    
    searching_phone = input('Введите номер телефона для поиска: ')
    print('\n')

    founded = False
    for line in temp_lst:
        if searching_phone in line and searching_phone == line.strip().split(',')[1].strip():
            print(line)
            founded = True
    if founded == False:
        print("Контакт с этим телефоном не найден. ")