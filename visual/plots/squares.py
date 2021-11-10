import matplotlib.pyplot as plt


def small():
    x = [3, 3, 3, 4, 4, 4, 3, 4]
    y = [3, 4, 3, 3, 3, 4, 4, 4]
    plt.plot(x, y, 'r:o')
    plt.show()


def medium():
    x = [2, 2, 2, 5, 5, 5, 2, 5]
    y = [2, 5, 2, 2, 2, 5, 5, 5]

    plt.plot(x, y, 'gs--')

    plt.show(small())


def large():
    x = [0, 6, 6, 6]
    y = [6, 6, 6, 0]

    plt.plot(x, y, 'bp-')

    plt.show(medium())


if __name__ == '__main__':
    large()
