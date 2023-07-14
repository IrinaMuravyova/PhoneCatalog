from const import FILE_PATH

def show_all_contacts() -> None:
    with open(FILE_PATH, 'r') as catalog:
        for line in catalog:
            print(line)

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