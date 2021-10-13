print("How many rows should i have?")
row = int(input())
print("\nHow many columns should i have?")
column = int(input())
print("\nHere i go:\n")
for x in range(0, row, 1):
    for y in range(0, column, 1):
        print(":-) ", end="")
    print()
print("\nDone!")
