# Задание 3
# Создайте иерархию классов с использованием множественного наследования. Выведите на экран
# порядок разрешения методов для каждого из классов. Объясните, почему линеаризации данных
# классов выглядят именно так.

class first:
    pass


class second:
    pass


class third(first):
    pass


class fourth(second):
    pass


class fifth(third, fourth):
    pass


def main():
    print(first.mro())
    print(second.mro())
    print(third.mro())
    print(fourth.mro())
    print(fifth.mro())

if __name__ == "__main__":
    main()