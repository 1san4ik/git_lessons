dict1 = {}
def func_a1():
    """Функция добавления новой ссылки в словарь"""
    longlink = input("Введите полную ссылку: ")
    shortlink = input("Введите сокращение для ссылки: ")
    dict1[shortlink] = longlink

def func_a2():
    """Функция получения ссылки из словаря"""
    shortlink2 = input("Введите сокращенную ссылку: ")
    if shortlink2 in dict1.keys():
        print(f"Ваша полная ссылка:  {dict1[shortlink2]}")
    else:
        print("Такой ссылки не вводилось. Попробуйте еще.")
