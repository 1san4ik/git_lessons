# Задание 2
# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть
# реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной
# ссылки по её названию.

dict1 = {}
while True:
    a = input("\nНажмите '1' - чтобы ввести ссылки в базу\nНажмите '2' - чтобы получить ссылку\nНажмите '3' - чтобы выйти\n=> ")
    if a == "1":
        longlink = input("Введите полную ссылку: ")
        shortlink = input("Введите сокращение для ссылки: ")
        dict1[shortlink] = longlink
    elif a == "2":
        shortlink2 = input("Введите сокращенную ссылку: ")
        if shortlink2 in dict1.keys():
            print(f"Ваша полная ссылка:  {dict1[shortlink2]}")
        else:
            print("Такой ссылки не вводилось. Попробуйте еще.")
    elif a == "3":
        print("*** Программа завершена ***")
        break
    else:
        print("Не корректный ввод.")
