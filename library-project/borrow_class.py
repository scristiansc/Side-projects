class Borrow:
    def __init__(self,checkout_id, book, user, checkout_date, return_date):
        self.checkout_id = checkout_id
        self.book = book
        self.checkout_date = checkout_date
        self.return_date = return_date


    def finish_borrow(self):
        print(f"""Borrowing book {self.book.title} finished.
        Must be returned by {self.user.name} before of {self.return_date}""")
