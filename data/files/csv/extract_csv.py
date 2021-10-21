import csv


def extract(path):
    print("Extracting...", end="")

    with open(path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names = ""
        for values in csv_reader:
            names += values[1] + "\n"
        print("Done!\nThe extracted names are as follows:")
        print(names)


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()
