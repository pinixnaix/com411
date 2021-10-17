def sum_weights(bop, beep):
    total = bop + beep
    return total


def cal_avg_weight(bop, beep):
    total = sum_weights(bop, beep) / 2
    return total


def run():
    print("What is the weight of Beep?")
    beep = int(input())
    print("\nWhat is the weight of Bop?")
    bop = int(input())
    print("\nWhat would you like to calculate ( sum or average )?")
    operation = input()
    if operation == 'sum':
        print(f"\nThe sum of Beep and Bop's weight is: {sum_weights(bop, beep)}")

    elif operation == 'average':
        print(f"\nThe average of Beep and Bop's weight is: {cal_avg_weight(bop, beep)}")


run()
