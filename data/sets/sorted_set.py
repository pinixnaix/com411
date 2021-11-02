def observed():
    observations = []
    for obs in range(5):
        print("Please enter an observation:")
        observations.append(input())
    return observations


def remove_observations(lista):
    y = 'yes'
    while y == 'yes':
        print("\nDo you wish to remove an observation (yes/no)?")
        y = input()
        if y != 'yes':
            break
        print("\nWhat observation do you wish to remove?")
        lista.remove(input())
        print("Done!")


def run():
    list_obs = observed()
    remove_observations(list_obs)
    observations = set()

    for obs in list_obs:
        observations.add((obs, list_obs.count(obs)))

    print("\nObservations:")
    sorted(observations)
    for x in observations:
        print(f"{x[0]} observed {x[1]} times.")


if __name__ == '__main__':
    run()
