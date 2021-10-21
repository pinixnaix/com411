import json


def read(path):
    with open(path) as file:
        data = json.load(file)
        print(f"City Name: {data['city']}")
        print(f"Population: {data['population']}")

        for bot in data['bots']:
            print(f"{bot['name']} ", end="")
            stats = bot['stats']
            print(f"has the strength level {stats['strength']} ", end="")
            print(f"and a speed level of {stats['speed']}")


def run():
    read("robocity.json")


if __name__ == "__main__":
    run()
