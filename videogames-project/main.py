from videogame import Videogame
from store import Store

# Videogames filling in the store
store = Store("Yate Games")

fifa25 = Videogame("Fifa 25", "PS5", 200_000, "sports")
ufc = Videogame("UFC", "PC", 150_000, "sports")
cod = Videogame("COD", "XBOX", 150_000, "FPS")

store.register_game(fifa25, 10)
store.register_game(ufc, 5)
store.register_game(cod, 5)

def prompt_user():
   print("-----------MAIN MENU: What would you like to do?----------")
   print("\n 1) List videogames")
   print("\n 2) Search for a videogame")
   print("\n 3) Buy a videogame")
   print("\n 4) Exit \n")

   return int(input("Select an option: "))

option = prompt_user()

while option != 4:
    if option == 1:
        print("\nLISTING VIDEOGAMES")
        store.show_stock()
    elif option == 2:
        print("Searching...")
        genre = input("Enter the genre of the videogame to search for: ")
        store.search_game_by_genre(genre)
    elif option == 3:
        game_id = int(input("Enter the ID of the video game to buy:"))
        quantity = int(input("Enter the quantity of the video game to buy:"))
        if quantity > store.stock_for_game(game_id):
            print("___________________________________________")
            print("WE DON'T HAVE THAT QUANTITY AVAILABLE,SORRY")
        else:
            store.buy_game(game_id, quantity)

    print("\n\n")
    option = prompt_user()