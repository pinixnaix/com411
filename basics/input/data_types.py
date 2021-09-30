# Beep calculates BMI
# Read in user data
user_name = input("What is your name human?\n")
user_age = int(input("\nHow old are you (in years)?\n"))
user_heigth = float(input("\nHow tall are you (in meters)?\n"))
user_weight = float(input("\nHow much do you weigh (in kilograms)?\n"))
# Calculate the BMI
user_bmi = user_weight/user_heigth**2
# Display result
print(f"\n{user_name} your are {user_age} and your bmi is {user_bmi:.2f}.")