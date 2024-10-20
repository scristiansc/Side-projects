class Library:
    def __init__(self):
        self.books = []
        self.users = []


    def register_user(self, user):
        self.users.append(user)
        print(f"User: {user.name} successfully registered! ")


    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"User {user.name} has been deleted.")


    def list_books(self):
        for book in self.books:
            print(book.show_info())


    def list_users(self):
        for user in self.users:
            print(f"{user.name}, Tel: {user.tel_number}")
