def display_ladder(steps):
    for x in range(steps):
        print("| |")
        print("***")
    print("| |")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)


create_ladder()
