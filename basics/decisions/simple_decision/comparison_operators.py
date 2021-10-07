# Asks the user to enter the first number

print("Please enter the first number.")
first = int(input())

# Asks the user to enter the second number

print("Please enter the second number.")
second = int(input())

if first < second:
    print("\nThe first number is the smallest!")
elif first > second:
    print("\nThe second number is the smallest!")
else:
    print("Both numbers are equal!")
