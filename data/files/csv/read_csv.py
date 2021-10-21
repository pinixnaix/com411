import csv


def read(path):
    with open(path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n {headings}")
        print("Values:")
        for line in csv_reader:
            print(line)


def run():
    read("bots.csv")


if __name__ == "__main__":
    run()
