import random

print("Please enter the minimum value:")
minimum = int(input())
print("Please enter the maximum value:")
maximum = int(input())
print("I am thinking of a number between 1 and 10. Can you guess what it is?")
guess = int(input())

prize = random.randint(minimum, maximum)

while guess != prize:
    if guess < prize:
        print("Your guess is too low.")
        print("Try again:")
        guess = int(input())
    elif guess > prize:
        print("Your guess is too high.")
        print("Try again:")
        guess = int(input())

print("Congratulations! You guessed my number!")
