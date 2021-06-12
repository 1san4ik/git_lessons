class Book:
    def __init__(self, autor, name_book, year, genre):
        self.autor = autor
        self.name_book = name_book
        self.year = year
        self.genre = genre


book_1 = Book("Andrzej Sapkowski", "The Witcher", "2016", "fantasy")
book_2 = Book(autor="Leo Tolstoy", name_book="War and Peace", year="1867", genre="historical novel")
book_3 = Book(autor="George Orwell", name_book="1984", year="1949", genre="dystopia")
