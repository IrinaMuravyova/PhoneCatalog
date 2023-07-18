from const import FILE_PATH, FILE_PATH_CSV
from prettytable import PrettyTable
from contacts import Contact
import csv

class ContactCatalog:
    def __init__(self, name: str = "Наши покупатели", contacts_list: list = None):
        if contacts_list is None:
            contacts_list = []
        self.name = name
        self.contacts_list = contacts_list
    

    def get_contacts(self, path) -> None:
        with open(path, 'r') as catalog:
            for line in catalog:
                line = line.strip().split(',')[0].split(' '),line.strip().split(',')[1]
                self.add_contact(Contact(*line[0], line[1]))
    

    def add_contact(self, contact: Contact) -> None:
        self.contacts_list.append(contact)


    def delete_contact(self, phone) -> None: # можно здесь запрашивать параметры для поиска нужной записи
        self.contacts_list.remove(self.search_phone(phone))


    def __str__(self):
        result_str = f'Имя справочника: {self.name}\n'
        for contact in self.contacts_list: # здесь можно добавить красивый вывод в таблицу
            result_str += f'\nФИО: {contact.surname} {contact.name} {contact.middlename}, телефон: {contact.phone_number}'
        return result_str
    

#     # def show_contacts(self) -> None:

#     #     table = PrettyTable()
#     #     table.field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]

#     #     catalog = self.get_contacts(FILE_PATH)
#     #     for line in catalog:
#     #         table.add_row(['{:<10}'.format(line.split(',')[0].split(' ')[0]), 
#     #                     '{:<10}'.format(line.split(',')[0].split(' ')[1]), 
#     #                     '{:<10}'.format(line.split(',')[0].split(' ')[2]), 
#     #                     line.split(',')[1]])
        
#     #     print(table)

    def search_contact(self) -> None:

        choose = int(input('\nПо какому параметру будем искать?'
                    '\n1: По имени'
                    '\n2: По фамилии'
                    '\n3: По отчеству'
                    '\n4: По номеру телефона'
                    '\n'))
        match choose:
            case 1:
                searching_name = input('Какое имя ищем: ')
                self.search_name(searching_name)
            
            case 2:
                searching_surname = input('Какую фамилию ищем: ')
                self.search_surname(searching_surname)

            case 3:
                searching_middlename = input('Какое отчество ищем: ')
                self.search_middlename(searching_middlename)

            case 4:   
                searching_phone = input('Какой номер телефона ищем: ')
                self.search_phone(searching_phone)


    def search_name(self, name) -> Contact:

        founded = False 
        for line in self.contacts_list:
            if name.strip().lower() == line.name.lower():
                founded = True
                print(line)
                return line
        if founded == False:
            print("Контакт с этим именем не найден. ")


    def search_surname(self, surname) -> Contact:


        founded = False
        for line in self.contacts_list:
            if surname.strip().lower() == line.surname.lower():
                founded = True
                print(line)
                return line
        if founded == False:
            print("Контакт с этой фамилией не найден. ")


    def search_middlename(self, middlename) -> Contact:

        founded = False
        for line in self.contacts_list:
            if middlename.strip().lower() == line.middlename.lower():
                founded = True
                print(line)
                return line
        if founded == False:
            print("Контакт с этим отчеством не найден. ")


    def search_phone(self, phone) -> Contact:

        founded = False
        for line in self.contacts_list:
            if phone.strip() == line.phone_number.strip():
                founded = True
                print(line)
                return line
        if founded == False:
            print("Контакт с этим телефоном не найден. ")
       

    def save_catalog(self) -> None:
        choose = int(input('\nС каким расширением сохранить файл:'
                    '\n1: .txt'
                    '\n2: .csv'
                    '\n'))
        match choose:
            case 1:
                self.export_txt(FILE_PATH)

            case 2:
                self.export_csv(FILE_PATH_CSV)
                

    def export_txt(self, FILE_PATH) -> None:

        with open(FILE_PATH, 'w') as catalog:
            for line in self.contacts_list:
                catalog.write(f'\n{line.surname} {line.name} {line.middlename}, {line.phone_number}')
        
        print("Файл экспортирован.")


    def export_csv(self, FILE_PATH_CSV) -> None:

        with open(FILE_PATH_CSV, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(self.contacts_list)
        
        print("Файл экспортирован.")


    def change_contact(self) -> None:

        choose = int(input('\nЧто будем менять?'
                    '\n1: Имя'
                    '\n2: Фамилию'
                    '\n3: Отчество'
                    '\n4: Номер телефона'
                    '\n5: ФИО'
                    '\n'))
        match choose:
            case 1:
                changing_name = input('Какое имя меняем: ')
                correct_name = input('Введите верное имя: ')
                self.change_name(changing_name, correct_name)
            
            case 2:
                changing_surname = input('Какую фамилию меняем: ')
                correct_surname = input('Введите верную фамилию: ')
                self.change_surname(changing_surname, correct_surname)

            case 3:
                changing_middlename = input('Какое отчество меняем: ')
                correct_middlename = input('Введите верное отчество: ')
                self.change_middlename(changing_middlename, correct_middlename)

            case 4:   
                changing_phone = input('Какой номер телефона меняем: ')
                correct_phone = input('Введите верный номер телефона: ')
                self.change_phone(changing_phone, correct_phone)

            case 5:   
                changing_fio = input('Какое ФИО меняем: ')
                correct_fio = input('Введите верное ФИО: ')
                self.change_fio(changing_fio, correct_fio)


    def change_name(self, wrong_name, right_name) -> None:
        for line in self.contacts_list:
            if line.name == wrong_name:
                line.name = right_name


    def change_surname(self, wrong_surname, right_surname) -> None:
        for line in self.contacts_list:
            if line.surname == wrong_surname:
                line.surname = right_surname

    def change_middlename(self, wrong_middlename, right_middlename) -> None:
        for line in self.contacts_list:
            if line.middlename == wrong_middlename:
                line.middlename = right_middlename

    def change_phone(self, wrong_phone, right_phone) -> None:
        for line in self.contacts_list:
            if line.phone == wrong_phone:
                line.phone = right_phone
    
    def change_fio(self, wrong_fio, right_fio) -> None:
        for line in self.contacts_list:
            if line.name == wrong_fio.split(',')[1] and line.surname == wrong_fio.split(',')[0] and line.middlename == wrong_fio.split(',')[2]:
                line.name == right_fio.split(',')[1]
                line.surname == right_fio.split(',')[0]
                line.middlename == right_fio.split(',')[2]