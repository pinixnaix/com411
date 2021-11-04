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


def menu2():
    print("*" * 85 + "\n" + " "*30 + "Olympics Games Statistics\n" + "*" * 85)
    print(f"""\nPlease select one of the following options:
           {"[all]":<10} Select Summer and Winter Olympics
           {"[summer]":<10} Select Summer Olympics
           {"[winter]":<10} Select Winter
           {"[exit]":<10} Exit the program
           """)
    print("Your selection:")
    return input().lower()


def menu(games):
    if games == 'all':
        print(" "*20 + "Summer and Winter Olympics Games Statistics\n" + "*" * 85)
    else:
        print("\n" + " "*25 + f"{games} Olympics Games Statistics\n" + "*" * 85)
    print(f"""\nPlease select one of the following options:
       {"[years]":<10} List unique years
       {"[tally]":<10} Tally up medals
       {"[team]":<10} Tally up medals for each team
       {"[athlete]":<10} Tally up medals for each athlete
       {"[back]":<10} Go Back
       """)
    print("Your selection:")
    return input().lower()


def display_medal_tally(tally):
    print(f"""
    {"| Gold":<10} | {tally.get("Gold")}{"|":>10}
    {"| Silver":<10} | {tally.get("Silver")}{"|":>10}
    {"| Bronze":<10} | {tally.get("Bronze")}{"|":>10}     
       """)


def display_years(years):
    for year in sorted(years, reverse=True):
        print(year)


def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")

        
def display_athlete_medal_tally(athlete_tally):
    for athlete, tally in athlete_tally.items():
        print(athlete)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")
