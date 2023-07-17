from const import FILE_PATH
from .get_contact import show_all_contacts


def delete_contact() -> None:

    with open(FILE_PATH, 'r') as catalog:
        catalog_copy = catalog.readlines()

    searching_contact = input('Введите какой контакт удалить(имя или фамилию или отчество или номер телефона): ')
    temp_lst = [line for line in catalog_copy if searching_contact  not in line]
    print(temp_lst)

    with open(FILE_PATH, 'w') as catalog:
        for line in temp_lst:
            catalog.write(line)


def change_contact() -> None:
    # with open("data.txt", 'r') as catalog:
    #     catalog_copy = catalog.readlines()
    pass

def add_contact() -> None:

    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    middlename = input("Введите отчество: ")
    phone_number= input("Введите номер телефона с кодом страны начиная с +: ")

    with open(FILE_PATH, 'a') as catalog:
        catalog.write(f'\n{name} {surname} {middlename}, {phone_number}')