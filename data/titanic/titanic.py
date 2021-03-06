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
  [5] Display the number of survivors per age group
  [6] Find a Passenger and display the line
  
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


def display_passengers_per_gender():
    females = 0
    males = 0

    for record in records:
        if record[4] == 'female':
            females += 1
        elif record[4] == 'male':
            males += 1

    print(f"Females: {females}, Males: {males}")


def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for record in records:
        if record[5] != '':
            age = float(record[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1

    print(f"Children: {children}, Adults: {adults}, Elderly: {elderly}")


def display_survivors_per_age_group():
    children = 0
    survived_children = 0
    adults = 0
    survived_adults = 0
    elderly = 0
    survived_elderly = 0

    for record in records:
        if record[5] != '':
            age = float(record[5])
            if age < 18:
                children += 1
                if record[1] == '1':
                    survived_children += 1
            elif age < 65:
                adults += 1
                if record[1] == '1':
                    survived_adults += 1
            else:
                elderly += 1
                if record[1] == '1':
                    survived_elderly += 1

    print(f"Children: {survived_children}/{children}, Adults: {survived_adults}/{adults}, Elderly: {survived_elderly}/{elderly}")


def find():
    print("Please enter the search parameters for the passenger's name:")
    name = input().lower()

    for record in records:
        if name in record[3].lower():
            print(f"{name} it is found in line {record[0]}")
            print(record)


def run():
    load_data("titanic.csv")

    print(f"Successfully loaded {len(records)} records.")

    selected_option = display_menu()
    print(f"You have selection option: {selected_option}\n")

    if selected_option == 1:
        display_passenger_names()

    elif selected_option == 2:
        display_num_survivors()

    elif selected_option == 3:
        display_passengers_per_gender()

    elif selected_option == 4:
        display_passengers_per_age_group()

    elif selected_option == 5:
        display_survivors_per_age_group()

    elif selected_option == 6:
        find()

    else:
        print("**** Error! Option not recognised! ****")


if __name__ == "__main__":
    run()
