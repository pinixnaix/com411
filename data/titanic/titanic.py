import csv
records = []
headings = []


def load_data(path):
    print("Loading data...", end="")

    with open(path) as file:
        csv_reader = csv.reader(file)
        headings.append(next(csv_reader))

        for x in csv_reader:
            records.append(x)
    print("Done!")


def run():
    load_data("titanic.csv")

    print(f"Successfully loaded {len(records)} records.")


if __name__ == "__main__":
    run()
