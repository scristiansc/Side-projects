from random import randrange

class Videogame():
    def __init__(self, title, platform, price, genre):
        self.id = randrange(10_000)
        self.title = title
        self.platform = platform
        self.price = price
        self.genre = genre

    def show_info(self):
        print(f"ID: {self.id}, Title: {self.title}, Price: {self.price}, Platform: {self.platform}, Genre: {self.genre}")
