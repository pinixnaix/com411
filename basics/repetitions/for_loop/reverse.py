print("What phrase do you see?")
phrase = str(input())

print("\n\nReversing...\n\n")
result = str()
for count in range(len(phrase)-1, -1, -1):
    result += (phrase[count])
print(f"The phrase is: {result}")
