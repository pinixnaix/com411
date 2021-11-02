def started(msg):
    print("*" * 85)
    print(f"Operation started: {msg}...\n")


def completed():
    print("Operation completed.")
    print("*" * 85)


def error(msg):
    print(f"Error! {msg}")


def menu():
    print(f"""Please select one of the following options:
       {"[years]":<10} List unique years
       {"[tally]":<10} Tally up medals
       {"[team]":<10} Tally up medals for each team
       {"[exit]":<10} Exit the program
       """)


def run():
    # started("hello")
    # completed()
    menu()


if __name__ == '__main__':
    run()
