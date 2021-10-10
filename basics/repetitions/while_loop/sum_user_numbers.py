print("How many numbers should i sum up?")
num = int(input())
x = 1
total = 0
print("")
while x <= num:
    print(f"Please enter number {x} of {num}")
    total += int(input())
    x += 1
print(f"\nThe answer is {total}.")
