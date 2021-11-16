import matplotlib.pyplot as plt


def read_data(path):
    data = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            data.append(int(line[0]))
            data.append(float(line[2:]))
    return data


def run():
    data = read_data("temps.txt")
    fig, (ax1, ax2) = plt.subplots(1, 2)
    x = []
    y = []
    for values in range(0, len(data), 2):
        x.append(data[values])
    for values in range(1, len(data), 2):
        y.append(data[values])

    ax1.plot(x, y)
    ax2.bar(x, y)
    ax1.set_xlabel('Day')
    ax1.set_ylabel('Temp')
    ax2.set_xlabel('Day')
    ax2.set_ylabel('Temp')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    run()
