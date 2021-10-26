def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run():
    value = likelihood()
    print(f"Minimum likelihood of falling: {min(value)}%")
    print(f"Maximum likelihood of falling: {max(value)}%")


if __name__ == "__main__":
    run()
