print("What strange markings do you see?")
marks = str(input())

print("\n\nIdentifying...\n\n")

for count in range(0, len(marks), 1):
    print(f"index {count}: {marks[count]}")
print("\n\nDone!")
