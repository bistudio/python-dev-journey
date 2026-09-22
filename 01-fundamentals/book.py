## create a book class for a library management cli

class Book:
    def __init__(self, title, author, ISBN, availability):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Availability: {self.availability}"
