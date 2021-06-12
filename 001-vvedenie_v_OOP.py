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
        if not isinstance(self, other):
            return False
        return self.autor == other.autor and self.name_book == other.name_book and self.year == other.year \
    and self.ganre == other.ganre


book_1 = Book(autor="Andrzej Sapkowski", name_book="The Witcher", year="2016", ganre="fantasy")
book_2 = Book(autor="Leo Tolstoy", name_book="War and Peace", year="1867", ganre="historical novel")
book_3 = Book(autor="George Orwell", name_book="1984", year="1949", ganre="dystopia")
book_1_copy = Book(autor="Andrzej Sapkowski", name_book="The Witcher", year="2016", ganre="fantasy")

print(book_1.__repr__())
print(book_1.__str__())
print(book_1 == book_2)
