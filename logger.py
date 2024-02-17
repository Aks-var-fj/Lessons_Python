from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('D:\Python\Task_8_Project\data_first_variant.csv', 'a', encoding='utf-8') as file: # открываем файл для добавления записи с кодировкой utf-8
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('D:\Python\Task_8_Project\data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

def print_data():
    print('1 файл: ')
    with open('D:\Python\Task_8_Project\data_first_variant.csv', 'r', encoding='utf-8') as file: # открываем файл для чтения с кодировкой utf-8
        data = file.readlines()
        print(''.join(data))
        
    print('2 файл: ')
    with open('D:\Python\Task_8_Project\data_second_variant.csv', 'r', encoding='utf-8') as file: # открываем файл для чтения с кодировкой utf-8
        data = file.readlines()
        print(''.join(data))

def copy_data():
    with open('D:\Python\Task_8_Project\data_first_variant.csv', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        print(list(contacts_list))
        for nn, contact in enumerate(contacts_list, 1):
            print(nn, contact, '\n')
        num_copy = int(input('Выберите номер контакта, который хотите скопировать: '))
    with open('D:\Python\Task_8_Project\data_second_variant.csv', 'a', encoding='utf-8') as file:
        file.write(f'{contacts_list[num_copy - 1]}\n\n')