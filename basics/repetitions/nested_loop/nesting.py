print("Please enter a sequence")
sequence = input()
print("\nPlease enter the character for the marker")
marker = input()

new_sequence = ""
distance = 0

for count in range(0, len(sequence), 1):
    if sequence[count] == marker:
        y = 1
        for x in range(count, len(sequence), 1):
            new_sequence = new_sequence + sequence[x]
            if sequence[x] == marker and x != count:
                print(new_sequence)
                break
    elif len(new_sequence) > 1:
        break
distance = len(new_sequence) - 2
print(f"\nThe distance between the markers is: {distance}")
