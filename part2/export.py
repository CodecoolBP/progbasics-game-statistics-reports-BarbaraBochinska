import reports

def export(file):
    filename = open("export.txt", "w")
    filename.write(str(reports.get_most_played("game_stat.txt")) + "\n")
    filename.write(str(reports.sum_sold("game_stat.txt")) + "\n")
    filename.write(str(reports.get_selling_avg("game_stat.txt")) + "\n")
    filename.write(str(reports.count_longest_title("game_stat.txt")) + "\n")
    filename.write(str(reports.get_date_avg("game_stat.txt")) + "\n")

export("game_stat.txt")

