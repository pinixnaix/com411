import json


def read(path):
    with open(path) as file:
        data = json.load(file)
        print(f"City Name: {data['city']}")
        print(f"Population: {data['population']}")

        for bot in data['bots']:
            print(f"{bot['name']} has the following stats:"
                  f"\n\t{bot['stats']}")


def run():
    read("robocity.json")


if __name__ == "__main__":
    run()
