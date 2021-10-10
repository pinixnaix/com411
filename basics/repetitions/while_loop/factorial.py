print("Please enter a number?")
num = int(input())
total = num

while num > 1:
    total *= (num - 1)
    num -= 1
print(f"\nThe factorial is {total}")
