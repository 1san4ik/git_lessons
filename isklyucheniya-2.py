# Задание 3
# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год
# поступления на работу. Конструктор должен генерировать исключение, если заданы неправильные
# данные. Введите список работников с клавиатуры. Выведите всех сотрудников, которые были приняты
# после заданного года.

class Worker:

    def __init__(self, name, surname, department, year):
        self.name = name
        self.surname = surname
        self.department = department
        self.year = year

    def showworker(self):
        print(f"Worker name: {self.name}, surname: {self.surname}, department: {self.department}, year: {self.year}")


def main():
    try:
        employee1 = Worker("Alex", "Ivanov", "IT", 2010)
        print(employee1)
        employee2 = Worker("Serg", "Smirnov", "Design", 2015)
        print(employee2)
        employee3 = Worker("Andrey", "Shtayler", "IT", 2020)
        print(employee3)
    except Exception:
        print("Данные введены не верно.")


if __name__ == '__main__':
    main()