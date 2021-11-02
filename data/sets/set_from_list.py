def observed():
    observations = []
    for obs in range(7):
        print("Please enter an observation:")
        observations.append(input())
    return observations


def run():
    print("Counting observations...")
    list_obs = observed()
    observations = set()
    for obs in list_obs:
        observations.add((obs, list_obs.count(obs)))
    print()
    for x in observations:
        print(f"{x[0]} observed {x[1]} times.")


if __name__ == '__main__':
    run()
