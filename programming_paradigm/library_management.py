class Book:
    """
    Represents a book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self.__is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out (unavailable).
        Returns True if successful, False if already checked out.
        """
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as returned (available).
        Returns True if successful, False if already available.
        """
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self.__is_checked_out

    def _str_(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book instances.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.__books = []  # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book instance to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return
        self.__books.append(book)

    def check_out_book(self, title):
        """
        Finds a book by title and marks it as checked out if available.

        Args:
            title (str): The title of the book to check out.
        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        for book in self.__books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Book with title '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """
        Finds a book by title and marks it as returned if checked out.

        Args:
            title (str): The title of the book to return.
        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        for book in self.__books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return True
                else:
                    print(f"'{title}' is already available.")
                    return False
        print(f"Book with title '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """
        Prints the title and author of all currently available books in the library.
        If no books are available, it prints a corresponding message.
        """
        available_found = False
        for book in self.__books:
            if book.is_available():
                print(book)  # Uses the _str_ method of the Book class
                available_found = True
        if not available_found:
            print("No books are currently available.")