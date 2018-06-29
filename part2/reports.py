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


