import reports
file_name = "game_stat.txt"

def most_played_game():
    print("What is the title of the most played game?")
    title = reports.get_most_played(file_name)
    print(title)

def total_sold():
    print("How many copies have been sold total? ")
    total = reports.sum_sold(file_name)
    print(total)

def avg_selling():
    print("What is the average selling?")
    avg = reports.get_selling_avg(file_name)
    print(avg)

def how_many_char():
    print("How many characters long is the longest title? ")
    char = reports.count_longest_title(file_name)
    print(char)

def avg_release():
    print("What is the average of the release dates? ")
    release = reports.get_date_avg(file_name)
    print(release)

def menu():
    print("1. What is the title of the most played game?")
    print("2. How many copies have been sold total?")
    print("3. What is the average selling?")
    print("4. How many characters long is the longest title?")
    print("5. What is the average of the release dates?")
    print("-----To exit input q------")

menu()
user_input = ""
while user_input != "q":
    user_input = input("\nInput number from 1 to 5 to ask a question: >>")
    if user_input == "1":
        most_played_game()

    if user_input == "2":
        total_sold()

    if user_input == "3":
        avg_selling()
        
    if user_input == "4":
        how_many_char()

    if user_input == "5":
        avg_release()