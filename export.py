import reports

def export(answer):
    filename = open("export.txt", "w")
    filename.write(str(reports.count_games(answer)) + "\n")
    filename.write(str(reports.decide(answer, 1998)) + "\n")
    filename.write(str(reports.get_latest(answer)) + "\n")
    filename.write(str(reports.count_by_genre(answer, "RPG")) + "\n")
    filename.write(str(reports.get_line_number_by_title(answer, "StarCraft")) + "\n")

export("game_stat.txt")