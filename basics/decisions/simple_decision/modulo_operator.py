# Asks the user to enter a whole number

print("Please enter a whole number.")

num = int(input())

if num % 2 == 0:
    print(f"\nThe number {num} is an even number.")
else:
    print(f"\nThe number {num} is an odd number.")