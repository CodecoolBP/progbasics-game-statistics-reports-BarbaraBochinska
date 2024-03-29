import reports
file_name = "game_stat.txt"

def how_many_games():
    print("How many games are in the file?")
    number = reports.count_games(file_name)
    print(number)

def game_from_year():
    year = input("Is there a game from a given year? ")
    answer = reports.decide(file_name, year)
    print(answer)

def latest_game():
    print("Which was the latest game?")
    game = reports.get_latest(file_name)
    print(game)

def how_many_games_by_genre():
    which_genre = input("How many games do we have by genre? ")
    game = reports.count_by_genre(file_name, which_genre)
    print(game)

def line_number_of_game():
    title = input("What is the line number of the given game? ")
    line_number = reports.get_line_number_by_title(file_name, title)
    print(line_number)

def menu():
    print("1. How many games are in the file?")
    print("2. Is there a game from a given year?")
    print("3. Which was the latest game?")
    print("4. How many games do we have by genre?")
    print("5. What is the line number of the given game?")
    print("-----To exit input q------")

menu()
user_input = ""
while user_input != "q":
    user_input = input("\nInput number from 1 to 5 to ask a question: >>")
    if user_input == "1":
        how_many_games()

    if user_input == "2":
        game_from_year()

    if user_input == "3":
        latest_game()
        
    if user_input == "4":
        how_many_games_by_genre()

    if user_input == "5":
        line_number_of_game()