1. Задание 1
# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе
# издания и жанре. Создайте несколько разных книг. Определите для него операции проверки на
# равенство и неравенство, методы __repr__ и __str__.

class Book:
    def __init__(self, autor, name_book, year, ganre):
        self.autor = autor
        self.name_book = name_book
        self.year = year
        self.ganre = ganre

    def __repr__(self):
        return f"Book (autor: {self.autor}, name: {self.name_book}, year: {self.year}, ganre: {self.ganre})"

    def __str__(self):
        return f"Book (autor: {self.autor}, name: {self.name_book}, year: {self.year}, ganre: {self.ganre})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.autor == other.autor and self.name_book == other.name_book and self.year == other.year \
            and self.ganre == other.ganre


book_1 = Book("Andrzej Sapkowski",
              "The Witcher",
              "2016",
              "fantasy")
book_2 = Book("Leo Tolstoy",
              "War and Peace",
              "1867",
              "historical novel")
book_3 = Book("George Orwell",
              "1984",
              "1949",
              "dystopia")
book_1_copy = Book("Andrzej Sapkowski",
                   "The Witcher",
                   "2016",
                   "fantasy")

print(repr(book_1))
print(str(book_2))
print(book_1 == book_1_copy)
print("*" * 60)

# 2. Задание 2
# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов. Сделайте
# так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.

class Books:
    def __init__(self, autor, name_book, year, ganre):
        self.autor = autor
        self.name_book = name_book
        self.year = year
        self.ganre = ganre
        self.review = []

    def __str__(self):
        line = f"Книга: '{self.name_book}' автор: {self.autor}, получила отзыв:\n"
        for i in self.review:
            line +=f"Отзыв: {str(i)} \n"
        return line

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.autor == other.autor and self.name_book == other.name_book and self.year == other.year \
            and self.ganre == other.ganre

    def add_review(self, review_text, user):
        rev = Review(review_text, user)
        self.review.append(rev)


class Review:
    def __init__(self, review_text, user):
        self.review_text = review_text
        self.user = user

    def __str__(self):
        return f"Пользователь {self.user}, оставил отзыв: '{self.review_text}'"


book_4 = Books("Andrzej Sapkowski",
              "The Witcher",
              "2016",
              "fantasy")
book_5 = Books("Leo Tolstoy",
              "War and Peace",
              "1867",
              "historical novel")
book_6 = Books("George Orwell",
              "1984",
              "1949",
              "dystopia")

rev_1 = input("Оставьте отзыв на книгу: ")
rev_2 = input("Напишите свое имя: ")
book_4.add_review(rev_1, rev_2)
print(book_4)
print("*" * 60)

# Задание 3
# Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
# Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и
# позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут
# быть заданы в одной шкале, а получены в другой.

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Температура ниже -273 невозможна")
        self._temperature = value


human = Celsius(int(input("Введите температуру: ")))
print(f"Температура по Цельсию: {human.temperature}")
print(f"Температура по Фаренгейту: {round(human.to_fahrenheit(), 2)}")

# Дополнительное задание
# Задание
# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
# автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.

# !!! C последним запутался, подскажите, что делать???

class СarShowroom:
    def __init__(self):
        self.list_auto = []

    def add_auto(self, brand, model, power, fuel, color):
        addavto = Auto(brand, model, power, fuel, color)
        self.list_auto.append(addavto)

    def sale(self, brand, model, power, fuel, color):
        pass


class Auto:
    def __init__(self, brand, model, power, fuel, color):
        self.brand = brand
        self.model = model
        self.power = power
        self.fuel = fuel
        self.color = color

    def __str__(self):
        return f"Автомобиль: Марка: {self.brand}, модель: {self.model},\
 мощность: {self.power}, топливо: {self.fuel}, цвет: {self.color}"

    def __eq__(self, other):
        if not isinstance(other, Auto):
            return False
        return self.brand == other.brand and self.model == other.model and self.power == other.power \
            and self.fuel == other.fuel and self.color == other.color


auto_1 = Auto("Mercedes", "S223", "4.6L", "benzine", "black")
auto_2 = Auto("VW", "Passat", "2.0L", "diesel", "blue")
auto_3 = Auto("BMW", "X5", "3.0L", "benzine", "brown")

print(str(auto_1))
