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


def display_menu():
    print("""
    
  Please select one of the following options:
  [1] Display the names of all passengers
  [2] Display the number of passengers that survived
  [3] Display the number of passengers per gender
  [4] Display the number of passengers per age group
 
  """)
    return int(input())


def run():
    load_data("titanic.csv")

    print(f"Successfully loaded {len(records)} records.")

    selected_option = display_menu()
    print(f"You have selection option: {selected_option}")


if __name__ == "__main__":
    run()
