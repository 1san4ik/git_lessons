# Задание 1
# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
# чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый
# интерфейс, и модуль представления, который отвечал бы за взаимодействие с пользователем. При
# замене последнего на другой, взаимодействующий с пользователем иным способом, программа
# должна продолжать корректно работать.

from Moduli_1_func import *
def main():
    """Это основная функция. В ней логика работы и обобщенный интерфейс"""
    while True:
        a = input("\nНажмите '1' - чтобы ввести ссылки в базу\nНажмите '2' - чтобы получить ссылку\nНажмите '3' - чтобы выйти\n=> ")
        if a == "1":
            func_a1()
        elif a == "2":
            func_a2()
        elif a == "3":
            print("*** Программа завершена ***")
            break
        else:
            print("Не корректный ввод.")

if __name__ == '__main__':
    main()