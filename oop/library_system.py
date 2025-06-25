# library_system.py

class Book:
    """
    Base class for all types of books.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    """
    Derived class for electronic books, inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    """
    Derived class for print books, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """
    Manages a collection of books using composition.
    """
    def __init__(self):
        self.books = []  # A list to store instances of Book, EBook, and PrintBook

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library.
        """
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only Book instances can be added to the library.")

    def list_books(self):
        """
        Prints details of each book in the library.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book):
                print(f"Book: {book.title} by {book.author}")