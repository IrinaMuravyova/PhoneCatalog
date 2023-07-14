from const import FILE_PATH


def delete_contact() -> None:

    with open(FILE_PATH, 'r') as catalog:
        catalog_copy = catalog.readlines()

    searching_name = input('Введите какой контакт удалить: ')
    temp_lst = [line for line in catalog_copy if searching_name not in line]

    with open(FILE_PATH, 'w', encoding='UTF-8') as catalog:
        for line in catalog_copy:
            catalog.write(line)

    print(catalog) # Почему-то не перезаписывает файл

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