def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run():
    value = likelihood()
    print(f"Minimum likelihood of falling: {value}%")


if __name__ == "__main__":
    run()
