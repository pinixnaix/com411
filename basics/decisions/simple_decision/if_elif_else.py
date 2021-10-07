print("Towards which direction should i paint (up, down, left or right)?")

direction = input().lower()

if direction == 'up':
    print(f"\nI am painting in the {direction}ward direction!")
elif direction == 'left':
    print(f"\nI am painting in the {direction}ward direction!")
elif direction == 'right':
    print(f"\nI am painting in the {direction}ward direction!")
elif direction == 'down':
    print(f"\nI am painting in the {direction}ward direction!")
else:
    print("\nThat is not a direction.")
