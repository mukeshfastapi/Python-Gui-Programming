# Introduction to aggregation

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add(self, book):
        self.books.append(book)

    def list_book(self):
        return [f'{book.name} and gener {book.title}' for book in self.books]


class Book:
    def __init__(self, name, titile):
        self.name = name
        self.title = titile


library = Library('Mukesh Library')

book1 = Book('Harry', 'Adventure')
book2 = Book('Python', 'Programing')

library.add(book1)
library.add(book2)

print(library.name)

for book in library.list_book():
    print(book)

