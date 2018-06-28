def count_games(file_name):
    file = open(file_name)
    how_many = len(file.readlines())
    file.close()
    return how_many
    

def decide(file_name, year):
    result = False
    year = str(year)
    file = open(file_name)
    if year in file.read():
        result = True
    else:
        result = False
    file.close()
    return result
    
def get_latest(file_name):
    


    
def count_by_genre(file_name, genre):
    pass
    
def get_line_number_by_title(file_name, title):
    pass