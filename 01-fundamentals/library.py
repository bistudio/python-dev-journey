## add a library class that manages a collection of books
from book import Book

class Library:
    def __init__(self):
        self.books = []
    ## add a book to the library collection
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
    ## list all books in the library
    def list_books(self):
        for book in self.books:
            print(book)
    ## find a book by its title
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    ## find a book by its author
    def find_book_by_author(self, author):
        for book in self.books:
            if book.author == author:
                return book
        return None
    ## find a book by its ISBN
    def find_book_by_ISBN(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                return book
        return None
    ## find a book by its availability
    def find_book_by_availability(self, availability):
        for book in self.books:
            if book.availability == availability:
                return book
        return None