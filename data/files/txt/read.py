def display_char(path, lenght):

    with open(path) as file:
        partial_data = file.read(lenght)
    print(f"The first {lenght} characters are:")
    print(partial_data)


def display_line(path):

    with open(path) as file:
        line = file.readline().strip()
    print("\nThe first line is:")
    print(line)


def display_text(path):
    with open(path) as file:
        data = file.read()
    print("\nThe full text is:")
    print(data)


def run():

    display_char("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()
