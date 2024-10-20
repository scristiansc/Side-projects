class User:
    def __init__(self, name, tel_number):
        self.name = name
        self.tel_number = tel_number
        self.borrowed_books = []


    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.update_availability(False)
            print(f"{book.title} borrowed to {self.name}.")
        else:
            print("This book cannot be borrowed,someone else has it checked out")


    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_availability(True)
            print (f"{book.title} was returned by {self.name}.")
        else:
            print("Sorry,you cannot return a book that you have not borrowed.")
