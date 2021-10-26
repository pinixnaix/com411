def directions():
    direct = ["Move Forward", "Move Backward", "Move Left", "Move Right"]

    return direct


def menu():
    print("Please select a direction:")
    direct = directions()
    for x in range(len(direct)):
        print(f"{x}: {direct[x]}")


def run():
    menu()


if __name__ == "__main__":
    run()
