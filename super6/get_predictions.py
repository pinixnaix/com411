import requests
from bs4 import BeautifulSoup
import csv
from csv import writer


def predictions(path, file):

    with open(file, 'w', newline='') as file:
        headings = ['MATCH', 'PROBABILITIES', 'BOTH TEAMS TO SCORE', 'OVER 2.5', 'HOME FORM', 'AWAY FORM', 'HEAD TO HEAD']
        csv_writer = writer(file)
        csv_writer.writerow(headings)

        result = requests.get(path)
        src = result.content

        soup = BeautifulSoup(src, 'html.parser')
        table = soup.find_all("table")
        predictions_table = table[0]
        stats = predictions_table.find_all("td")
        for x in range(0, len(stats), 8):
            match = stats[x].text
            probs = stats[x+1].text.split()
            btts = stats[x+2].text.split()
            over = stats[x+3].text.split()
            home = stats[x+4].text.split()
            away = stats[x+5].text.split()
            head = stats[x+6].text.split()
            csv_writer.writerow([match, probs, btts, over, home, away, head])


def display_games(path):
    predictions("https://www.footstats.co.uk/index.cfm?task=forecast_premier", 'predictions.csv')
    with open(path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        print("***    FIXTURES    ***\n")
        x = 1
        for line in csv_reader:
            match = line[0].split()
            match.pop(0)
            match.pop(0)
            if len(match) == 3:
                print(f"[{x}] {match[0]} VS {match[2]}")
            elif len(match) == 5:
                print(f"[{x}] {match[0]} {match[1]} VS {match[3]} {match[4]}")
            elif len(match) == 4:
                a = match[1]
                if a[0] == '[':
                    print(f"[{x}] {match[0]} VS {match[2]} {match[3]}")
                else:
                    print(f"[{x}] {match[0]} {match[1]} VS {match[3]}")
            x += 1


def display_menu():
    print("""

  Please select one of the following options:
  [1] Display the next matches in the premier league

  """)
    return int(input())


def run():

    selected_option = display_menu()
    print(f"You have selection option: {selected_option}\n")

    if selected_option == 1:
        display_games('predictions.csv')

    else:
        print("**** Error! Option not recognised! ****")


if __name__ == '__main__':
    run()
