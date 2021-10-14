def cross_bridge(steps):
    if steps > 5:
        for count in range(6):
            print("Crossed Step")
        print("The bridge is collapsing!")
    else:
        for count in range(steps):
            print("Crossed Step")
        print("We must keep going!")


cross_bridge(3)
cross_bridge(6)
