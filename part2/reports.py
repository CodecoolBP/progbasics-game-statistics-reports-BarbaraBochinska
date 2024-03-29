def get_most_played(file_name):
    with open (file_name, "r") as file:
        lines = file.readlines()
    sale = []
    titles = []
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        sale.append(float(lines[i][1]))   
        titles.append(lines[i][0])
    biggest_sale = sale.index(max(sale))
    game_title = titles[biggest_sale]
    return game_title

def sum_sold(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    sold_games = []
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        sold_games.append(float(lines[i][1]))
    total_sum = sum(sold_games)
    return total_sum

def get_selling_avg(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    sold_games = []
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        sold_games.append(float(lines[i][1]))
    total_sum = sum(sold_games)
    avg_sale = total_sum / len(lines)
    return avg_sale

def count_longest_title(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    titles = []
    length = []
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        titles.append(lines[i][0])
        length.append(len(titles[i]))
    longest_length = max(length)
    return longest_length

def get_date_avg(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    release_dates = []
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        release_dates.append(int(lines[i][2]))
    sum_dates = sum(release_dates)
    avg_release_float = sum_dates / len(lines)
    avg_release = round(avg_release_float)
    return avg_release

def get_game(file_name, title):
    with open(file_name, "r") as file:
        read_file = file.read()
        lines = read_file.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        if title == lines[i][0]:
            chosen_title = lines[i]
            formatted_chosen_title = [chosen_title[0],float(chosen_title[1]),int(chosen_title[2]),chosen_title[3],chosen_title[4]]
    return formatted_chosen_title   