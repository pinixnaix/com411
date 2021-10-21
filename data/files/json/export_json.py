import json


def read(path):
    print("Reading...", end="")
    with open(path) as file:
        data = json.load(file)
    print("Done!")
    return data


def save(path, data):
    print("Exporting...", end="")
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    print("Done!")


def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)


if __name__ == "__main__":
    run()
