from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the _str_ method
    print(my_book)  # Expected to use _str_

    # Demonstrating the _repr_ method
    print(repr(my_book))  # Expected to use _repr_

    # Deleting a book instance to trigger _del_
    del my_book

if _name_ == "_main_":
    main()