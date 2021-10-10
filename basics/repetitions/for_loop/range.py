print("What level of brightness is required?")
level = int(input())
print("\nAdjusting brightness...")
for count in range(2, level + 2, 2):
    print(f"\nBeep's brightness level: {'*'* count}")
    print(f"Bop's brightness level: {'*' * count}")
print("\nAdjustments complete!")
