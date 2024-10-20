class Librarians:
    def __init__(self, librarian_id, name):
        self.librarian_id = librarian_id
        self.name = name


    def add_book(self, library, book):
        library.books.append(book)
        print(f"Book: {book.title} added successfully.")


    def remove_book(self, library, book):
        if book in library.books:
            library.books.remove(book)
            print(f"Book: {book.title} has been deleted")
        else:
            print("This book is not in the library system")
