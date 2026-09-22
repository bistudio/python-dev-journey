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
    ## find book by class attribute, such as title, author, ISBN, or availability
    ## availability should return a list of books that is available
    def find_book_by_attribute(self, attribute, value):
        for book in self.books:
            if hasattr(book, attribute) and getattr(book, attribute) == value:
                if attribute == "availability":
                    return [b for b in self.books if b.availability == value]
                return book
        return None
    ## remove a book from the library collection
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
    ## checkout a book from the library
    def checkout_book(self, book):
        if book in self.books and book.availability:
            book.availability = False
            return True
        return False
    ## return a book or books to the library
    def return_book(self, book):
        if isinstance(book, list):
            success = False
            for b in book:
                if b in self.books and not b.availability:
                    b.availability = True
                    success = True
            return success
        else:
            if book in self.books and not book.availability:
                book.availability = True
                return True
        return False