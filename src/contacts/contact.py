class Contact:
    
    def __init__(self, surname, name, middlename, phone):

        self.surname = surname
        self.name = name
        self.middlename = middlename
        self.phone_number = phone
    
    def __str__(self):
        return(f'{self.surname} {self.name} {self.middlename}, {self.phone_number}')    
        
        # table = PrettyTable()
        # table.field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]

        # table.add_row(['{:<10}'.format(self.surname), 
        #                '{:<10}'.format(self.name), 
        #                '{:<10}'.format(self.middlename), 
        #                 self.phone_number])
        # print(table)
        # return ''