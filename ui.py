from logger import * # импортирует все функции из файла logger

def interface():
    print("Добрый день! Это бот-помощник. \n"
          "Что вы хотите сделать? \n"
          "1 - Записать данные \n"
          "2 - Вывести данные \n"
          "3 - Копировать данные \n")
    command = int(input("Ваш выбор: "))
    while command < 1 or command > 4:
        command = int(input("Ошибка! Ваш выбор: "))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        copy_data()
interface()
    


"""Дополнить справочник возможностью(функциями) копирования данных из одного файла в другой.
Пользователь вводит номер данных, которую необходимо перенести из одного файла в другой.
ИЛИ
Добавить возможность удаления и изменения данных в файлах."""