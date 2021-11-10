import matplotlib.pyplot as plt


def coordinate():
    x = input("Please enter an x value")
    y = input("Please enter an y value")
    coordinates = (x, y)
    return coordinates


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for val in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]


def run():
    values = path()
    plt.plot(values[0], values[1], 'r--o')
    plt.xlabel('x_values')
    plt.ylabel('y_values')
    plt.show()


if __name__ == '__main__':
    run()
