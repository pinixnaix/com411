print("How many bars should be charged?")
bars = int(input())
x = 0
print("")
while x < bars:
    print("Charging: ", end="")
    x += 1
    print(f"{'⬛' * x}")
print("\nThe battery is fully charged.")
