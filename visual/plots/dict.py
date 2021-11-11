import matplotlib.pyplot as plt
import random


def data():
    paths = {}
    print("Please enter the type of line you want to use (:, -- or -)")
    paths['linestyle'] = input()
    print("Please enter the colour of line you want to use (r, g or b)")
    paths['color'] = input()
    print("Please enter the style of marker you want to use (o, s or ^)")
    paths['marker'] = input()
    return paths


def generate():
    print("How many lines would you like to display?")
    lines = int(input())

    for line in range(lines):
        values = data()
        x = random.sample(range(1, 10), 5)
        y = random.sample(range(1, 10), 5)
        plt.plot(x, y, **values)

    plt.show()


def run():
    print("Running...")
    generate()
    print("Done!")


if __name__ == '__main__':
    run()
