import csv
import os

def save_game(game_number, countries_guessed):
    filename="Countriesguessed.csv"
    games={}


    if os.path.exists(filename):
        with open (filename,'r',encoding='utf-8') as file:
            reader=csv.reader(file)
            headers=next(reader,None)
            if headers:
                for col_index, header in enumerate(headers):
                    game_num=int(header.replace("Game ", "").replace(" Guess", ""))
                    games[game_num]=[]
                    for row in reader:
                        for col_index, value in enumerate(row):
                            if value:
                                game_num=int(headers[col_index].replace("Game ", "").replace(" Game", ""))
                                games[game_num].append(value)
    games[game_number]=countries_guessed

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer=csv.writer(file)
        sorted_games=sorted(games.keys())
        writer.writerow([f"Game {g} Guess" for g in sorted_games])
        max_rows=max(len(games[g]) for g in sorted_games)
        for i in range(max_rows):
            row=[]
            for g in sorted_games:
                row.append(games[g][i] if i < len(games[g]) else "")
                writer.writerow(row)