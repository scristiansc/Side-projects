class Store():
    def __init__(self, name):
        self.name = name
        self.__games = [] #Inventory
        self.__stock = {}

    def register_game(self, videogame, quantity):
        if videogame not in self.__games:
            self.__games.append(videogame)
            self.__stock[videogame.id] = quantity

    def show_stock(self):
        for game in self.__games:
            game.show_info()
            print(f"Units Available: {self.__stock[game.id]} ")

    def buy_game(self, game_id, quantity):
        for game in self.__games:
            if game.id == game_id:
                #Subtract quantity from inventory
                self.__stock[game_id] -= quantity
                print(f"Total purchase price: ${game.price * quantity}")
                return
        print("¡INVALID ID!")

    def search_game_by_title(self, title):
        for game in self.__games:
            if game.title == title:
                print(f"The game {game.title} has been found!")
                game.show_info()
                print(f"There are {self.__stock[game.title]} units available")
                return
        print("¡GAME NOT FOUND!")


    def search_game_by_genre(self, genre):
        games_found = False

        for game in self.__games:
            if game.genre == genre:
                games_found = True
                game.show_info()
                print(f"There are{self.__stock[game.id]} units available")
        if not games_found:
            print("¡There are NO games with that genre!")


    def stock_for_game(self, game_id):
        return self.__stock[game_id]