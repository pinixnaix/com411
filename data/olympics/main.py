import csv
import process
import tui


def read_data(file_path,games):
    tui.started("Reading data from {file_path}")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        data = []
        for line in csv_reader:
            if line[10].lower() == games:
                data.append(line)
            if line[10].lower() == games:
                data.append(line)
            elif games == 'all':
                data.append(line)
    tui.completed()
    return data


def run2(athlete_data,games):
    while True:
        selection = tui.menu(games)
        if selection == "years":
            process.list_years(athlete_data)
        elif selection == "tally":
            process.tally_medals(athlete_data)
        elif selection == "team":
            process.tally_team_medals(athlete_data)
        elif selection == "back":
            run()
        else:
            tui.error("Invalid Selection!")


def run():

    while True:
        selection = tui.menu2()
        if selection == "summer":
            athlete_data = read_data("athlete_events.csv",selection)
            run2(athlete_data,selection)
        elif selection == "winter":
            athlete_data = read_data("athlete_events.csv",selection)
            run2(athlete_data,selection)
        elif selection == "all":
            athlete_data = read_data("athlete_events.csv",selection)
            run2(athlete_data,selection)
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()
