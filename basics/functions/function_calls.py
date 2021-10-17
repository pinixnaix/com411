def display_box(word):
    print("\n###" + '#' * len(word) + "###")
    print("#  " + ' ' * len(word) + "  #")
    print("#  " + ' ' * len(word) + "  #")
    print("#  " + word + "  #")
    print("#  " + ' ' * len(word) + "  #")
    print("#  " + ' ' * len(word) + "  #")
    print("###" + '#' * len(word) + "###")


def display_lower(word):
    print("\n" + word.lower())


def display_upper(word):
    print("\n" + word.upper())


def display_mirror(word):
    mirror = ""
    for letter in word:
        mirror = letter + mirror
    print("\n" + word + ' | ' + mirror)


def repeat(word):
    new_word = ""
    y = 1
    for x in range(len(word)):
        if y == 1:
            new_word = new_word + word[x].upper()
            y = 0
        else:
            new_word = new_word + word[x].lower()
            y = 1

    print("How many times do you want the word repeated?")
    times = int(input())
    print("\n" + (new_word + " ") * times)


def run():
    print("Please enter a word")
    word = input()
    print("\nPlease choose from one of the following options:")
    print("\n1) Display in a Box")
    print("2) Display Lower-case")
    print("3) Display Upper-case")
    print("4) Display Mirrored")
    print("5) Repeat")
    option = input()

    if option == '1':
        display_box(word)

    elif option == '2':
        display_lower(word)

    elif option == '3':
        display_upper(word)

    elif option == '4':
        display_mirror(word)

    elif option == '5':
        repeat(word)


run()
