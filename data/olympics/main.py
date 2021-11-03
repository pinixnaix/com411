import csv
#import process
import tui


def read_data(file_path):
    tui.started("Reading data from {file_path}")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        data = []
        for line in csv_reader:
            data.append(line)
    tui.completed()
    return data


def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            pass
        elif selection == "tally":
            pass
        elif selection == "team":
            pass
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()
