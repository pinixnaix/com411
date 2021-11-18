import csv
import matplotlib.pyplot as plt


def read_data(path):
    data = {}
    with open(path) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        week1 = [0]
        week2 = [0]
        for row in csv_reader:
            week1.append(int(row[0]))
            week2.append(int(row[1]))
        data[header[0]] = week1
        data[header[1]] = week2
    return data


def run():
    data = read_data('temps.csv')
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex='col')

    ax1.plot(data.get('week1'))
    ax2.plot(data.get('week2'))
    ax1.set_xlim(1, 7)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    run()
