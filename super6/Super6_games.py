import requests
from bs4 import BeautifulSoup
import csv
from csv import writer
import pandas as pd


def get_fixtures(path, file):

    with open(file, 'w', newline='') as file:
        headings = ['MATCH', 'PROBABILITIES', 'BOTH TEAMS TO SCORE', 'OVER 2.5', 'HOME FORM', 'LINKHOME',
                    'AWAY FORM', 'LINKAWAY', 'HEAD TO HEAD', 'LINKHEAD', 'LINKSTATS']
        csv_writer = writer(file)
        csv_writer.writerow(headings)

        result = requests.get(path)
        src = result.content

        soup = BeautifulSoup(src, 'html.parser')
        table = soup.find_all("table")
        predictions_table = table[0]
        stats = predictions_table.find_all("td")
        links = []
        for link in predictions_table.find_all("a"):
            links.append(link.get('href'))

        for x in range(0, len(stats), 8):
            del links[0]
            del links[0]
            match = stats[x].text
            probs = stats[x + 1].text.split()
            btts = stats[x + 2].text.split()
            over = stats[x + 3].text.split()
            home = stats[x + 4].text.split()
            linkhome = links[0]
            del links[0]
            away = stats[x + 5].text.split()
            linkaway = links[0]
            del links[0]
            head = stats[x + 6].text.split()
            linkhead = links[0]
            del links[0]
            linkstats = links[0]
            del links[0]
            csv_writer.writerow([match, probs, btts, over, home, linkhome, away, linkaway, head,
                                 linkhead, linkstats])


def display_games(path):
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


def super6_fixtures(in_path, out_path, fix):
    with open(in_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        with open(out_path, 'a') as file2:
            csv_writer = writer(file2)
            x = 1
            for row in csv_reader:
                if x in fix:
                    csv_writer.writerow(row)
                x += 1

    df = pd.read_csv(out_path)
    df.to_csv(out_path, index=False)


def select_super6_fixtures():
    with open('super6_fixtures.csv', 'w') as file:
        headings = ['MATCH', 'PROBABILITIES', 'BOTH TEAMS TO SCORE', 'OVER 2.5', 'HOME FORM', 'LINKHOME',
                    'AWAY FORM', 'LINKAWAY', 'HEAD TO HEAD', 'LINKHEAD', 'LINKSTATS']
        csv_writer = writer(file)
        csv_writer.writerow(headings)

    print("Select this week Super 6 ")
    display_games('fixtures_premier.csv')
    print("How many games to you want to select from the premier League")
    games = int(input())
    fixtures = []
    for counter in range(games):
        print(f"Select game  {counter + 1}")
        fixtures.append(int(input()))
    super6_fixtures('fixtures_premier.csv', 'super6_fixtures.csv', fixtures)

    display_games('fixtures_championship.csv')
    print("How many games to you want to select from the Championship")
    games = int(input())
    fixtures1 = []
    for counter in range(games):
        print(f"Select game  {counter + 1}")
        fixtures1.append(int(input()))
    super6_fixtures('fixtures_championship.csv', 'super6_fixtures.csv', fixtures1)


def display_menu():
    print("""
  Please select one of the following options:
  [1] Update the Fixtures
  [2] Display Fixtures
  [3] Select Super 6 Fixtures
  [4] Display Super 6 Fixtures
  """)
    return int(input())


def display_menu_fixtures():
    print("""
              Please select one of the following options:
              [1] Display the Fixtures for Premier League
              [2] Display the Fixtures for the Championship
              [3] Go back to main menu
              """)
    fix = int(input())
    if fix == 1:
        display_games('fixtures_premier.csv')
        display_menu_fixtures()
    elif fix == 2:
        display_games('fixtures_championship.csv')
        display_menu_fixtures()
    elif fix == 3:
        run()
    else:
        print("**** Error! Option not recognised! ****")


def run():
    selected_option = display_menu()

    print(f"You have selection option: {selected_option}\n")
    if selected_option == 1:
        print("Updating....", end='')
        get_fixtures("https://www.footstats.co.uk/index.cfm?task=forecast_premier", 'fixtures_premier.csv')
        get_fixtures("https://www.footstats.co.uk/index.cfm?task=forecast_championship", 'fixtures_championship.csv')
        print("Done!!!")
        run()

    elif selected_option == 2:
        display_menu_fixtures()

    elif selected_option == 3:
        select_super6_fixtures()
        run()
    elif selected_option == 4:
        display_games('super6_fixtures.csv')

    else:
        print("**** Error! Option not recognised! ****")


if __name__ == '__main__':
    run()
