def started(msg):
    print("*" * 85)
    print(f"Operation started: {msg}...\n")


def completed():
    print("Operation completed.")
    print("*" * 85)


def error(msg):
    print(f"Error! {msg}")


def menu():
    print("Please select one of the following options:")


def run():
    # started("hello")
    # completed()
    menu()


if __name__ == '__main__':
    run()
