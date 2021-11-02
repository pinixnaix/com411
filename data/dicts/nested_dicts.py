def short_pattern():
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def run():
    print("Analysing patterns...")
    pattern_dict = {"short sequence": short_pattern(), "medium sequence": medium_pattern(),
                    "long sequence": long_pattern()}
    for keys, values in pattern_dict.items():
        print(f"{keys}: {values}")


if __name__ == '__main__':
    run()
