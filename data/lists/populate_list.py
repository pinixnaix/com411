def directions():
    direct = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

    return direct


def menu():
    print("\nPlease select a direction:")
    direct = directions()
    for x in range(len(direct)):
        print(f"{x}: {direct[x]}")
    return direct[int(input())]


def run():
    route = []
    print("Working out escape route...")

    for x in range(5):
        route.append(menu())

    print(f"Escape route: {route}")


if __name__ == "__main__":
    run()
