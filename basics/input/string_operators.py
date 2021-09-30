# Improve Beep's health
# Read in user data
number_lives = int(input("Please enter number of lives.\n"))
energy_level = int(input("\nPlease enter energy level.\n"))
shield_level = int(input("\nPlease enter the shield level.\n"))
print("\nHealth has been set.\n")

# Display output

print(f"Lives: {'❤'*number_lives}")
print(f"Energy: {'✬'*energy_level}")
print(f"Shield: {'✠'*shield_level}")
