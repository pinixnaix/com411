import csv


def extract(path, number):
    print("Exporting...")

    with open(path, "a") as file:

        for x in range(number):
            print("Please enter the bot id:")
            bot_id = input()

            print("Please enter the bot name:")
            bot_name = input()

            print("Please enter the bot paint:")
            bot_paint = input()

            file.write(f"\n{bot_id},{bot_name},{bot_paint}")
        print("Done!")


def run():
    extract("exported_bots.csv", 2)


if __name__ == "__main__":
    run()
