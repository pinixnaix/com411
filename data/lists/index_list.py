def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    movement = movements()
    print(f"{movement[0]} for  {movement[1]}  steps")
    print(f"{movement[2]} for  {movement[3]}  steps")
    print(f"{movement[4]} for  {movement[5]}  steps")
    print(f"{movement[6]} for  {movement[7]}  steps")


if __name__ == "__main__":
    run()
