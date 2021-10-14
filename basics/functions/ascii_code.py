print("Program Started!")
print("Please enter a character:")
character = input()
if len(character) == 1:
    print(f"The ASCII code for {character} is: ", ord(character))
else:
    print("!!ERROR!! Entered more than 1 character!!")
print("Program Ended!")
