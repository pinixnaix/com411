import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.ascii_art as ascii_art
import basics.output.escape_characters as escape_characters


def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        print()
        simple_message.run()
        print()
    elif response == "multiline_message":
        print()
        multiline_message.run()
        print()
    elif response == "ascii_art":
        print()
        ascii_art.run()
        print()
    elif response == "escape_characters":
        print()
        escape_characters.run()
        print()
    else:
        print("Invalid Program! Please try again.\n")
        run_block_a()


def run():

    while True:
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")


run()
