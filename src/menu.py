import actions

def start_menu() -> None:
    while True:
        choose = int(input('\nВыберите пункт меню: '
                        '\n1. Вывести все контакты '
                        '\n2. Поиск контакта по имени'
                        '\n3. Поиск контакта по фамилии'
                        '\n4. Поиск контакта по отчеству'
                        '\n5. Поиск контакта по номеру телефона'
                        '\n6. Удалить контакт'
                        '\n7. Изменить контакт'
                        '\n8. Добавить контакт'
                        '\n9. Сохранить контакт'
                        '\n0. Выход из меню'
                        '\n --> '))
        
        match choose:
            case 1:
                actions.show_all_contacts()
            case 2:
                actions.search_name()
            case 3:
                actions.search_surname()
            case 4:
                actions.search_middlename()
            case 5:
                actions.search_phone_number()
            case 6:
                actions.delete_contact()
            case 7:
                actions.change_contact()
            case 8:
                actions.add_contact()
            case 9:
                actions.save_contact()
            case 0:
                break
