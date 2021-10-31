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
            probs = stats[x+1].text
            btts = stats[x+2].text
            over = stats[x+3].text
            home = stats[x+4].text
            away = stats[x+5].text
            head = stats[x+6].text
            csv_writer.writerow([match.encode(), probs.encode(), btts.encode(), over.encode(), home.strip(), away.strip(), head.strip()])


def display_games(path):
    predictions("https://www.footstats.co.uk/index.cfm?task=forecast_premier", 'predictions.csv')
    with open(path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n {headings}")
        print("Values:")
        for line in csv_reader:
            print(line)


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
