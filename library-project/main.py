from book_class import Book
from librarians_class import Librarians
from library_class import Library
from user_class import User

#Creando una instancia de biblioteca
my_library = Library()

#Signing up librarians
librarian = Librarians(10, "Gabriel")

#Creating some books
book1 = Book("El alquimista", "Paulo Coelho", 1988)
book2 = Book("Cien años de soledad", "Gabriel garcia Marquez", 1967)

#Adding books to the library
print("||||ADDING NEW BOOKS TO THE SYSTEM||||\n")
librarian.add_book(my_library, book1)
librarian.add_book(my_library, book2)

print("-------------------------------------------------\n")

#Creating users
user1 = User("Nicolas", 3004567867)
user2 = User("Fil", 3014567898)

#Signing up users
print("||||ADDING NEW USERS TO THE SYSTEM||||\n")
my_library.register_user(user1)
my_library.register_user(user2)

print("-------------------------------------------------\n")
#Book borrow
print(f"||||{user1.name} is borrowing a new book||||\n")
user1.borrow_book(book1)
print("-------------------------------------------------\n")

#Diferent user tries to borrow the same book
print(f"||{user2.name},is trying to borrow the same book as {user1.name}||\n")
print("ALERT!")
user2.borrow_book(book1)
print("-------------------------------------------------\n")

#User return the book
print(f"||||{user1.name} returned the book||||\n")
user1.return_book(book1)
print("-------------------------------------------------\n")

#User tries to return a book they never borrowed
print(f"||{user2.name},is trying to return a book he never borrowed||\n")
print("ALERT!")
user1.return_book(book1)
print("-------------------------------------------------\n")

print("||TOTAL BOOKS REGISTERED ON THE SYSTEM||\n")
my_library.list_books()
print("-------------------------------------------------\n")
print("||TOTAL USERS REGISTERED ON THE SYSTEM||\n")
my_library.list_users()