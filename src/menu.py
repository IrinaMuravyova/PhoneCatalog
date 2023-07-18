from loader import curCatalog
from const import FILE_PATH


def start_menu() -> None:

    while True:
        choose = int(input('\nВыберите пункт меню: '
                        '\n1. Вывести все контакты '
                        '\n2. Найти контакт'
                        '\n3. Изменить контакт'
                        '\n4. Добавить контакт'
                        '\n5. Удалить контакт'
                        '\n6. Сохранить справочник'
                        '\n0. Выход из меню'
                        '\n --> '))
        
        match choose:

            case 1:
                print(curCatalog)

            case 2:
                curCatalog.search_contact()

            case 3:
                curCatalog.change_contact()

            case 4:
                new_surname = input('Введите фамилию: ')
                new_name = input('Введите имя: ')
                new_middlename = input('Введите отчество: ')
                new_phone = input('Введите номер телефона: ')
                curCatalog.add_contact([new_surname, new_name, new_middlename, new_phone])

            case 5:
                searching_contact = input('Введите какой контакт удалить(номер телефона): ')
                curCatalog.delete_contact(searching_contact.strip())

            case 6:
                curCatalog.save_catalog()
                
            case 0:
                break
