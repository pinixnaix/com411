# A little program to guess the results of Super6 using Lisa's method

print("\tWelcome to this week SUPER 6!!!\n")

home_team = int()
away_team = int()

iterations = 1
import random

while iterations < 7:

    print(f"\t\t\tGAME {iterations}")
    home = random.randint(0, 5)
    away = random.randint(0, 5)
    print(f"\tHome Team {home} - {away} Away Team ")
    iterations = iterations + 1

print("\nGood luck for this week SUPER 6"
      "\n This is the way to beat Jeff!!"
      "\n\t\tLisa v1.0")
