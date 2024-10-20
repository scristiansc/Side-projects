class Book:
    def __init__(self, title, author, year_publication):
        self.title = title
        self.author = author
        self.year_publication = year_publication
        self.available = True


    def show_info(self):
        return f"{self.title} by {self.author}"


    def update_availability(self, available):
        self.available = available
        status = "available" if available else "unavailable"
        print (f"{self.title} is now {status}")