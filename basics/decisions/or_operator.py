print("What type of adventure should i have?")

adventure = str(input()).lower()

if adventure == 'scary' or adventure == 'short':
    print("\nEntering the dark forest!")

elif adventure == 'safe' or adventure == 'long':
    print("\nTaking the safe route!")
else:
    print("Not sure which route to take")
