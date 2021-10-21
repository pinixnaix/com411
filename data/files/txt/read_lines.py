def search(path):
    print("Searching...")
    with open(path) as file:
        for line in file:
            print(f"Looked in {line}")
    print("...Done!")


def run():

    search("library.txt")


if __name__ == "__main__":
    run()
