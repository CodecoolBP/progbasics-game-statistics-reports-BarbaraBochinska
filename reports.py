def count_games(file_name):
    with open (file_name, "r") as file:
        how_many = len(file.readlines())
    return how_many

def decide(file_name, year):
    result = False
    year = str(year)
    file = open(file_name)
    if year in file.read():
        result = True
    else:
        result = False
    
    return result

def get_latest(file_name):
    with open (file_name, "r") as file:
        lines = file.readlines()
    years = []
    titles = []
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        years.append(lines[i][2])   
        titles.append(lines[i][0])
        latest_year = years.index(max(years))
        latest_game_title = titles[years.index(max(years))]
    return latest_game_title

def count_by_genre(file_name, genre):
    with open (file_name, "r") as file:
        lines = file.readlines()
    genres = []
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        genres.append(lines[i][3])
    return genres.count(genre)

def get_line_number_by_title(file_name, title):
    with open (file_name, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        try:
            if title in lines[i]:
                line_number = lines.index(lines[i])
                line_number += 1
        except:
            raise ValueError
    return line_number    