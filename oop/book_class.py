# book_class.py

class Book:
    def __init__(self, title, author, year):
        """
        Initializes a Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor: Prints a message upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation: Returns a user-friendly string for the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Returns a string that can recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

if __name__ == '__main__':
    # Example Usage:
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("1984", "George Orwell", 1949)

    print("\n--- String Representations ---")
    print(book1)  # Uses _str_
    print(book2)

    print("\n--- Official Representations ---")
    print(repr(book1)) # Uses _repr_
    print(repr(book2))

    print("\n--- Deleting Objects ---")
    # Objects will be deleted when they go out of scope or explicitly with del
    del book1
    # book2 will be deleted automatically when the script ends