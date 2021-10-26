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


def display_passenger_names():
    print("The names of the passengers are...\n")

    for record in records:
        passenger_name = record[3]
        print(passenger_name)


def display_num_survivors():
    num_survived = 0

    for record in records:
        if record[1] == '1':
            num_survived += 1

    print(f"{num_survived} passengers survived")


def run():
    load_data("titanic.csv")

    print(f"Successfully loaded {len(records)} records.")

    selected_option = display_menu()
    print(f"You have selection option: {selected_option}\n")

    if selected_option == 1:
        display_passenger_names()

    elif selected_option == 2:
        display_num_survivors()

    else:
        print("**** Error! Option not recognised! ****")


if __name__ == "__main__":
    run()
