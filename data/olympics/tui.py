def started(msg):
    print("*" * 85)
    print(f"Operation started: {msg}...\n")


def completed():
    print("\nOperation completed.")
    print("*" * 85)


def error(msg):
    print("*" * 85)
    print(" " * 30 + f"Error! {msg}")
    print("*" * 85)


def menu():
    print(f"""\nPlease select one of the following options:
       {"[years]":<10} List unique years
       {"[tally]":<10} Tally up medals
       {"[team]":<10} Tally up medals for each team
       {"[exit]":<10} Exit the program
       """)
    print("Your selection:")
    return input()


def display_medal_tally(tally):
    print(f"""
    
    | Gold      |{tally.get("Gold")}     |
    | Silver    |{tally.get("Silver")}   |
    | Bronze    |{tally.get("Bronze")}   | 
       
       """)


def display_years(years):
    for year in sorted(years, reverse=True):
        print(year)


def display_team_medal_tally(team_tally):
    for team in team_tally:
        print(team)
        for key, values in team_tally.items():
            print(f"\t{key}:{values} ", end='')
        print()
