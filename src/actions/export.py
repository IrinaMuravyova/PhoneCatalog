from const import FILE_PATH, FILE_PATH_CSV
import csv

def save_contact() -> None:
    choose = int(input('\nС каким расширением хотите сохранить файл:'
                   '\n1: .txt'
                   '\n2: .csv'
                   '\n'))
    match choose:
        case 1:
            pass
        case 2:
            with open(FILE_PATH, 'r') as catalog:
                catalog_copy = catalog.readlines()

            with open(FILE_PATH_CSV, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(catalog_copy)
            
            print("Файл экспортирован.")