# Asks the user to enter where to look

print("Where should i look?")
place = str(input()).lower()

if place == 'in the bedroom':
    print("Where in the bedroom should i look?")
    bedroom = str(input()).lower()

    if bedroom == 'under the bed':
        print("Found some shoes but no battery!")
    else:
        print("Found some mess but no battery!")

elif place == 'in the bathroom':
    print("Where in the bathroom should i look?")
    bathroom = str(input()).lower()

    if bathroom == 'in the bathtub':
        print("Found a rubber duck but no battery!")
    else:
        print("Found a wet surface but no battery!")

elif place == 'in the lab':
    print("Where in the lab should i look?")
    lab = str(input()).lower()

    if lab == 'on the table':
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery!")

else:
    print("I do not know where that is but i will keep looking!")
