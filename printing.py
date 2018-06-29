import reports
file_name = "game_stat.txt"

print("1. How many games are in the file?")
print("2. Is there a game from a given year?"))
print("3. Which was the latest game?")
print("4. How many games do we have by genre?")
print("5. What is the line number of the given game?")

user_input = ("Input number from 1 to 5 to ask a question: ")

print("How many games are in the file?")
number = reports.count_games(file_name)
print(number)

year = input("Is there a game from a given year? ")
answer = reports.decide(file_name, year)
print(answer)

print("Which was the latest game?")
game = reports.get_latest(file_name)
print(game)

which_genre = input("How many games do we have by genre? ")
game = reports.count_by_genre(file_name, which_genre)
print(game)

title = input("What is the line number of the given game? ")
line_number = reports.get_line_number_by_title(file_name, title)
print(line_number)