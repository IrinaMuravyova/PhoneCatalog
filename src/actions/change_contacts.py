from const import FILE_PATH
from .get_contact import show_all_contacts


def delete_contact() -> None:

    with open(FILE_PATH, 'r') as catalog:
        catalog_copy = catalog.readlines()

    searching_contact = input('Введите какой контакт удалить(имя или фамилию или отчество или номер телефона): ')
    temp_lst = [line for line in catalog_copy if searching_contact  not in line]

    with open(FILE_PATH, 'w') as catalog:
        for line in temp_lst:
            catalog.write(line)


def change_contact() -> None:
    
    with open(FILE_PATH, 'r') as catalog:
        catalog_copy = catalog.readlines()

    temp_lst=[]

    changing_contact = input('Введите какой контакт хотите изменить(ФИО): ')
    new_fio = input('Введите новое значение ФИО: ')
    new_phone_number = input('Введите новое значение номера телефона: ')
    
    for line in catalog_copy:
        if changing_contact.lower() in line.lower():
            line = f'{new_fio}, {new_phone_number}'
        temp_lst.append(line)    

    with open(FILE_PATH, 'w') as catalog:
        for line in temp_lst:
            catalog.write(line)

def add_contact() -> None:

    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    middlename = input("Введите отчество: ")
    phone_number= input("Введите номер телефона с кодом страны начиная с +: ")

    with open(FILE_PATH, 'a') as catalog:
        catalog.write(f'\n{surname} {name} {middlename}, {phone_number}')