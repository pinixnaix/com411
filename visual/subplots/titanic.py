import csv
import matplotlib.pyplot as plt


def read_data(path):
    data = {"survived": [], "sex": [], "age": [], "fare": []}
    with open(path) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        for row in csv_reader:
            survived = row[1].strip()
            sex = row[14].strip()
            age = row[4].strip()
            fare = row[8].strip()
            if survived != "" and sex != "" and age != "" and fare != "":
                data["survived"].append(int(survived))
                data["age"].append(float(age))
                data["fare"].append(round(float(fare), 2))
                if int(sex) == 0:
                    data["sex"].append("Female")
                else:
                    data["sex"].append("Male")
    return data


def run():
    data = read_data('titanic.csv')

    fig, axes = plt.subplots(2, 2)
    axes[0, 0].plot(data.get('survived'))
    axes[0, 1].plot(data.get('sex'))
    axes[1, 0].plot(data.get('age'))
    axes[1, 1].plot(data.get('fare'))
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    run()
